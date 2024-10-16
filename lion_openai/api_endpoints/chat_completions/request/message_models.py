from typing import List, Literal, Optional, TypeAlias

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .types import Detail


class TextContentPart(BaseModel):
    type: Literal["text"] = Field(description="The type of the content part.")
    text: str = Field(description="The text content.")


class ImageURL(BaseModel):
    url: str = Field(description="The URL of the image.")
    detail: Detail = Field("auto", description="The detail level of the image.")
    model_config = ConfigDict(use_enum_values=True)


class ImageContentPart(BaseModel):
    type: Literal["image_url"] = Field(description="The type of the content part.")
    image_url: ImageURL = Field(description="The image URL and detail level.")


ContentPart: TypeAlias = TextContentPart | ImageContentPart


class Function(BaseModel):
    name: str = Field(description="The name of the function to call.")
    arguments: str = Field(
        description="The arguments to call the function with, as JSON."
    )


class ToolCall(BaseModel):
    id: str = Field(description="The ID of the tool call.")
    type: Literal["function"] = Field(
        description="The type of the tool. Only 'function' is supported."
    )
    function: Function = Field(description="The function that the model called.")


class SystemMessage(BaseModel):
    role: Literal["system"]
    content: str = Field(description="The content of the system message.")

    name: Optional[str] = Field(
        None,
        description="An optional name for the participant."
        " Provides the model information "
        "to differentiate between participants of the same role.",
    )


class UserMessage(BaseModel):
    role: Literal["user"]
    content: str | List[ContentPart] = Field(
        description="The content of the user message"
    )

    name: Optional[str] = Field(
        None,
        description="An optional name for the participant."
        " Provides the model information "
        "to differentiate between participants of the same role.",
    )


class AssistantMessage(BaseModel):
    role: Literal["assistant"]
    content: Optional[str] = Field(
        None,
        description="The contents of the assistant message."
        " Required unless tool_calls is specified.",
    )

    refusal: str | None = Field(
        None, description="The refusal message by the assistant."
    )

    name: Optional[str] = Field(
        None,
        description="An optional name for the participant."
        " Provides the model information "
        "to differentiate between participants of the same role.",
    )

    tool_calls: Optional[List[ToolCall]] = Field(
        None,
        description="The tool calls generated by the model," " such as function calls.",
    )

    @model_validator(mode="after")
    def validate_content(self):
        if not self.content and not self.tool_calls:
            raise ValueError("Assistant messages require content or tool_calls")
        return self


class ToolMessage(BaseModel):
    role: Literal["tool"]
    content: str | list = Field(description="The contents of the tool message.")

    tool_calls_id: str = Field(
        description="Tool call that this message is responding to."
    )


Message: TypeAlias = SystemMessage | UserMessage | AssistantMessage | ToolMessage
