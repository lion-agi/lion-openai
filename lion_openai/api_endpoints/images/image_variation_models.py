from typing import IO, Optional, Literal
from enum import Enum
from pydantic import Field, field_validator, ConfigDict
from ..data_models import OpenAIEndpointRequestBody


class Size(str, Enum):
    S256 = "256x256"
    S512 = "512x512"
    S1024 = "1024x1024"


class OpenAIImageVariationRequestBody(OpenAIEndpointRequestBody):
    image: str | IO = Field(
        description="The image to use as the basis for the variation(s). "
                    "Must be a valid PNG file, less than 4MB, and square.",
    )

    model: Optional[Literal["dall-e-2"]] = Field(
        "dall-e-2", description="The model to use for image generation."
    )

    n: int | None = Field(
        1, description="The number of images to generate.", ge=1, le=10
    )

    response_format: Optional[Literal["url", "b64_json"]] = Field(
        "url",
        description="The format in which the generated images are returned.",
    )

    size: Optional[Size] = Field(
        "1024x1024", description="The size of the generated images."
    )

    user: Optional[str] = Field(
        None,
        description="A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.",
    )

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_validator("image")
    @classmethod
    def get_file_object(cls, value):
        if isinstance(value, str):
            value = open(value, "rb")
        return value

    def __del__(self):
        # Ensure files are closed when the object is destroyed
        image_obj = self.__dict__.get("image")
        if image_obj and not image_obj.closed:
            image_obj.close()