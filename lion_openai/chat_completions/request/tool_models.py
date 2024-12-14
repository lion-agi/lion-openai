from typing import Any, Literal

from pydantic import BaseModel, Field


class FunctionParameters(BaseModel):
    type: Literal["object"] = "object"
    properties: dict[str, dict[str, Any]]
    required: list[str] | None = None


class Function(BaseModel):
    description: str | None = Field(
        None,
        description=(
            "A description of what the function does, used by the model to "
            "choose when and how to call the function."
        ),
    )

    name: str = Field(
        max_length=64,
        pattern="^[a-zA-Z0-9_-]+$",
        description=(
            "The name of the function to be called. Must be a-z, A-Z, 0-9, "
            "or contain underscores and dashes, with a maximum length of 64."
        ),
    )

    parameters: FunctionParameters | None = Field(
        None,
        description=(
            "The parameters the functions accepts, described as a JSON Schema "
            "object. See the guide for examples, and the JSON Schema "
            "reference for documentation about the format."
        ),
    )

    strict: bool | None = Field(
        False,
        description="Whether to enable strict schema"
        " adherence when generating the function call. "
        "If set to true, the model will follow the exact"
        " schema defined in the parameters field. "
        "Only a subset of JSON Schema is supported when strict is true.",
    )


class Tool(BaseModel):
    type: Literal["function"] = Field(
        description="The type of the tool. Currently,"
        " only function is supported."
    )
    function: Function = Field(description="The function definition.")
