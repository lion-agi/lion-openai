from typing import Literal
from pydantic import BaseModel, Field


class Name(BaseModel):
    name: str = Field(description="The name of the function to call.")


class ToolChoice(BaseModel):
    type: Literal["function"] = Field(
        description="The type of the tool. Currently, only function is supported."
    )
    function: Name = Field(description="Specifies the function to be called.")
