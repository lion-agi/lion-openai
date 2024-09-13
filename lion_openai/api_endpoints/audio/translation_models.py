from typing import Optional

# translation.py
from pydantic import Field
from ..data_models import OpenAIEndpointRequestBody, OpenAIEndpointResponseBody
from .types import WhisperModel, TranscriptionResponseFormat


class OpenAITranslationRequestBody(OpenAIEndpointRequestBody):
    file: bytes = Field(description="The audio file to translate")
    model: WhisperModel = Field(description="The model to use for translation")
    prompt: Optional[str] = Field(
        None,
        description="An optional text to guide the model's style or continue a previous audio segment",
    )
    response_format: TranscriptionResponseFormat = Field(
        default=TranscriptionResponseFormat.JSON,
        description="The format of the transcript output",
    )
    temperature: float = Field(
        default=0, ge=0, le=1, description="The sampling temperature"
    )


class OpenAITranslationResponseBody(OpenAIEndpointResponseBody):
    text: str = Field(description="The translated text")
