from typing import List, Optional

from pydantic import BaseModel, Field

from ..data_models import OpenAIEndpointRequestBody


class Image(BaseModel):
    b64_json: Optional[str] = Field(
        None,
        description="The base64-encoded JSON of the generated image, if response_format is b64_json.",
    )

    url: Optional[str] = Field(
        None,
        description="The URL of the generated image, if response_format is url (default).",
    )

    revised_prompt: Optional[str] = Field(
        None,
        description="The prompt that was used to generate the image, if there was any revision to the prompt.",
    )


class OpenAIImageResponseBody(OpenAIEndpointRequestBody):
    created: int = Field(
        description="The Unix timestamp of when the image was created."
    )

    data: List[Image] = Field(description="The list of generated images.")
