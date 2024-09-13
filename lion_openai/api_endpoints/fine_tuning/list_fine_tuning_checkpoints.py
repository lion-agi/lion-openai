from typing import List, Optional, Literal
from pydantic import Field, ConfigDict
from ..data_models import (
    OpenAIEndpointPathParam,
    OpenAIEndpointQueryParam,
    OpenAIEndpointResponseBody,
)
from .fine_tuning_job_checkpoint_models import OpenAIFineTuningJobCheckpointResponseBody


class OpenAIListFineTuningCheckpointsPathParam(OpenAIEndpointPathParam):
    fine_tuning_job_id: str = Field(
        description="The ID of the fine-tuning job to get checkpoints for."
    )


class OpenAIListFineTuningCheckpointsQueryParam(OpenAIEndpointQueryParam):
    after: Optional[str] = Field(
        None,
        description="Identifier for the last checkpoint ID from the previous pagination request.",
    )

    limit: Optional[int] = Field(
        10, description="Number of checkpoints to retrieve.", ge=1
    )


class OpenAIListFineTuningCheckpointsResponseBody(OpenAIEndpointResponseBody):
    object: Literal["list"] = Field(
        description="The object type, always 'list' for a list of fine-tuning checkpoints.",
    )

    data: List[OpenAIFineTuningJobCheckpointResponseBody] = Field(
        description="A list of fine-tuning checkpoints."
    )

    first_id: str = Field(description="The ID of the first checkpoint in the list.")

    last_id: str = Field(description="The ID of the last checkpoint in the list.")

    has_more: bool = Field(
        description="Whether there are more results available after this batch."
    )