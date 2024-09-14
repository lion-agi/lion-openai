from pydantic import Field
from ..data_models import OpenAIEndpointPathParam


class OpenAIDeleteFineTunedModelPathParam(OpenAIEndpointPathParam):
    model: str = Field(description="The model to delete.")
