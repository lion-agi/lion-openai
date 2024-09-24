from pydantic import BaseModel, Field


class Usage(BaseModel):
    completion_tokens: int = Field(
        description="Number of tokens in the generated completion."
    )

    prompt_tokens: int = Field(description="Number of tokens in the prompt.")

    total_tokens: int = Field(
        description="Total number of tokens used in the"
        " request (prompt + completion)"
    )
