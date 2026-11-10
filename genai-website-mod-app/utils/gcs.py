# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import base64
import random
from enum import Enum
from typing import Any

import requests
from google.cloud import storage
from PIL import Image


class ContentState(Enum):
    PRODUCTION = "PRODUCTION"
    DRAFT = "DRAFT"
    REVIEW = "REVIEW"


def parseStorageUrl(url: str) -> tuple[str, str]:
    if url.startswith("https://"):
        gcs_url = url.replace("https://storage.googleapis.com/", "")
        bucket = gcs_url.split("/")[0]
        blob = gcs_url.replace(f"{bucket}/", "")
    elif url.startswith("gs://"):
        # gs://<bucket>/draft/1.html
        bucket = url.replace("gs://", "").split("/")[0]
        blob = url.replace(f"gs://{bucket}/", "")  # noqa: E231
    return bucket, blob


def upload_images(images: Any, project_id: str, bucket_name: str) -> list[str]:
    image_urls = []

    # Handle New google-genai Imagen response (GenerateImagesResponse)
    if hasattr(images, "generated_images"):
        for img in images.generated_images:
            img_byte_arr = io.BytesIO()
            img.image.save(img_byte_arr, format="PNG")
            url = upload_file(
                binary_content=img_byte_arr.getvalue(),
                project_id=project_id,
                blob_name=f"images/imagen-{random.randrange(1, 10000000)}.png",
                bucket_name=bucket_name.lower(),
                content_type="image/png",
            )
            image_urls.append(url)

    # Handle Gemini GenerativeModel response (GenerationResponse)
    elif hasattr(images, "candidates"):
        for candidate in images.candidates:
            for part in candidate.content.parts:
                pil_image = None
                # Prioritize the pre-parsed .image attribute from google-genai SDK
                if hasattr(part, "image") and part.image:
                    pil_image = part.image
                elif hasattr(part, "inline_data") and part.inline_data:
                    try:
                        decoded_data = base64.b64decode(part.inline_data.data)
                        pil_image = Image.open(io.BytesIO(decoded_data))
                    except Exception as e:
                        print(f"[Warning] Failed to identify image in inline_data: {e}")
                        continue

                if pil_image:
                    img_byte_arr = io.BytesIO()
                    pil_image.save(img_byte_arr, format="PNG")
                    url = upload_file(
                        binary_content=img_byte_arr.getvalue(),
                        project_id=project_id,
                        blob_name=f"images/genai-{random.randrange(1, 10000000)}.png",
                        bucket_name=bucket_name.lower(),
                        content_type="image/png",
                    )
                    image_urls.append(url)

    # Handle Legacy Imagen response (ImageGenerationResponse)
    elif hasattr(images, "images"):
        for img in images.images:
            # Refactor to use PIL for consistency and standard formatting
            pil_image = Image.open(io.BytesIO(img._image_bytes))
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format="PNG")
            url = upload_file(
                binary_content=img_byte_arr.getvalue(),
                project_id=project_id,
                blob_name=f"images/imagen-{random.randrange(1, 10000000)}.png",
                bucket_name=bucket_name.lower(),
                content_type="image/png",
            )
            image_urls.append(url)

    print(f"image_urls={image_urls}")
    return image_urls


def copy_file(
    project_id: str,
    source_bucket: str,
    source_blob: str,
    new_bucket: str,
    new_blob: str,
) -> str:
    storage_client = storage.Client(project=project_id)

    source_bucket_client = storage_client.bucket(source_bucket)
    source_blob_client = source_bucket_client.blob(source_blob)
    destination_bucket = storage_client.bucket(new_bucket)

    blob_copy = source_bucket_client.copy_blob(
        source_blob_client, destination_bucket, new_blob
    )

    return blob_copy.public_url


def move_file(
    project_id: str,
    source_bucket: str,
    source_blob: str,
    new_bucket: str,
    new_blob: str,
) -> str:
    storage_client = storage.Client(project=project_id)

    source_bucket_client = storage_client.bucket(source_bucket)
    source_blob_client = source_bucket_client.blob(source_blob)
    destination_bucket = storage_client.bucket(new_bucket)

    # destination_generation_match_precondition = 0

    blob_copy = source_bucket_client.copy_blob(
        source_blob_client, destination_bucket, new_blob
    )
    source_blob_client.delete()

    return blob_copy.public_url


def upload_file(
    binary_content: Any,
    project_id: str,
    bucket_name: str,
    blob_name: str,
    content_type="image/png",
) -> str:
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name.lower())
    blob = bucket.blob(blob_name.lower())
    blob.upload_from_string(binary_content, content_type=content_type)

    return blob.public_url


def download_file_from_url(url: str) -> bytes:
    try:
        response = requests.get(url)
        print("[Info]Download file from url")
        return response.content
    except Exception as e:
        print(f"[Error]Unable to download file: {e}")
        return bytes()


def download_file(project_id: str, bucket_name: str, blob_name: str) -> bytes:
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    if blob.exists():
        print("[Info]Download file")
        return blob.download_as_bytes()
    else:
        print(f"[Warning]{blob_name} does not exists")
        return bytes()


def list_files(project_id: str, bucket_name: str, file_prefix: str = "") -> list[dict]:
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    if file_prefix is not None and file_prefix != "":
        blobs = bucket.list_blobs(prefix=file_prefix)
    else:
        blobs = bucket.list_blobs()
    return [
        {
            "name": "gs://" + bucket_name + "/" + blob.name,
            "storage_class": blob.storage_class,
            "public_url": blob.public_url,
        }
        for blob in blobs
        if not blob.name.endswith("/")
    ]


def delete_file(project_id: str, bucket_name: str, blob_name: str) -> None:
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()
