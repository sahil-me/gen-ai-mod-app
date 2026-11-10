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

import os
import sys

from fastapi import APIRouter
from google import genai
from google.genai import types

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


router = APIRouter()


def caption_image(image_bytes: bytes, model_name="imagen-3.0-generate-002") -> list[str]:
    """Uses Gemini to describe an image."""
    client = genai.Client()
    image_part = types.Part.from_bytes(data=image_bytes, mime_type="image/png")
    response = client.models.generate_content(
        model=model_name,
        contents=[image_part, "Provide a short caption for this image."]
    )
    return [response.text]


def generate_image(prompt: str, negative_prompt: str = "", model_name="imagen-3.0-generate-002"):
    """Uses Gemini to generate an image."""
    client = genai.Client()
    # Incorporate negative prompt instructions directly into the main prompt
    full_prompt = f"{prompt}\nAvoid: {negative_prompt}" if negative_prompt else prompt
    response = client.models.generate_content(
        model=model_name,
        contents=full_prompt
    )
    return response


def edit_image(image_bytes: bytes, prompt: str, model_name="imagen-3.0-generate-002"):
    """Uses Gemini to edit an image based on multimodal instructions."""
    client = genai.Client()
    image_part = types.Part.from_bytes(data=image_bytes, mime_type="image/png")
    response = client.models.generate_content(
        model=model_name,
        contents=[image_part, prompt]
    )
    return response
