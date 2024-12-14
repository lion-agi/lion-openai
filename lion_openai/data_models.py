from pydantic import BaseModel, ConfigDict

config = {
    "use_enum_values": True,
    "validate_assignment": True,
}


class OpenAIEndpointRequestBody(BaseModel):
    model_config = ConfigDict(extra="forbid", **config)


class OpenAIEndpointResponseBody(BaseModel):
    model_config = ConfigDict(**config)


class OpenAIEndpointQueryParam(BaseModel):
    model_config = ConfigDict(extra="forbid", **config)


class OpenAIEndpointPathParam(BaseModel):
    model_config = ConfigDict(extra="forbid", **config)
