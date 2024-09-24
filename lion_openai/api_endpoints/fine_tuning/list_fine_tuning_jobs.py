from typing import List, Literal, Optional

from pydantic import Field

from ..data_models import OpenAIEndpointQueryParam, OpenAIEndpointResponseBody
from .fine_tuning_job_models import OpenAIFineTuningJobResponseBody


class OpenAIListFineTuningJobsQueryParam(OpenAIEndpointQueryParam):
    after: Optional[str] = Field(
        None,
        description="Identifier for the last job from the previous pagination request.",
    )

    limit: Optional[int] = Field(
        20, description="Number of fine-tuning jobs to retrieve.", ge=1
    )


class OpenAIListFineTuningJobsResponseBody(OpenAIEndpointResponseBody):
    object: Literal["list"] = Field(
        description="The object type, always 'list' for a list of fine-tuning jobs.",
    )

    data: List[OpenAIFineTuningJobResponseBody] = Field(
        description="A list of fine-tuning job events."
    )

    has_more: bool = Field(
        description="Whether there are more results available after this batch."
    )
