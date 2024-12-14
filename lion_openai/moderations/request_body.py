from enum import Enum

from pydantic import Field

from ..data_models import OpenAIEndpointRequestBody


class Model(str, Enum):
    LATEST = "text-moderation-latest"
    STABLE = "text-moderation-stable"


class OpenAIModerationRequestBody(OpenAIEndpointRequestBody):
    input: list | str = Field(description="The input text to classify")

    model: Model | None = Field(
        "text-moderation-latest",
        description="Two content moderations models are available: text-moderation-stable and text-moderation-latest.",
    )
