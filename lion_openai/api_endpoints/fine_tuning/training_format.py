from typing import List, Optional

from pydantic import BaseModel, Field, SerializeAsAny

from ..chat_completions.request.request_body import Message, Tool


class OpenAIChatModelTrainingFormat(BaseModel):
    messages: SerializeAsAny[List[Message]] = Field(
        description="A list of messages comprising the conversation so far."
    )

    tools: Optional[List[Tool]] = Field(
        None, description="A list of tools may generate JSON inputs for."
    )

    parallel_tool_calls: Optional[bool] = Field(
        True,
        decription="Whether to enable parallel function calling during tool use.",
    )


class OpenAICompletionsModelTrainingFormat(BaseModel):
    prompt: str = Field(description="The input prompt for this training example.")

    completion: str = Field(
        description="The desired completion for this training example."
    )
