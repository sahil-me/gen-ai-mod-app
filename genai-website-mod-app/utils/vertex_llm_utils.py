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

from google import genai

def llm_generate(
    prompt: str,
    model_name: str = "gemini-2.5-flash",
    max_output_tokens: int = 2048,
    temperature: float = 0.0,
    top_p: float = 0.8,
    top_k: int = 40,
) -> str:
    client = genai.Client()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=genai.types.GenerateContentConfig(
            max_output_tokens=max_output_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
        )
    )

    return response.text


def llm_code_generate(prompt: str, model_name: str = "gemini-2.5-flash") -> str:
    client = genai.Client()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=genai.types.GenerateContentConfig(
            max_output_tokens=8192,
            temperature=0.0,
        )
    )

    return response.text


def llm_generate_gemini(prompt: str, model_name: str = "gemini-2.5-flash") -> str:
    client = genai.Client()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=genai.types.GenerateContentConfig(
            max_output_tokens=8192,
            temperature=0.0,
        )
    )

    return response.text
