from os import getenv
from io import IOBase
import aiohttp
from pydantic import BaseModel, Field, field_validator

from .data_models import OpenAIEndpointRequestBody, OpenAIEndpointQueryParam, OpenAIEndpointPathParam


class OpenAIRequest(BaseModel):

    api_key: str = Field(description="API key for authentication", exclude=True)

    openai_organization: str | None = Field(
        default=None, description="Organization id", exclude=True
    )

    openai_project: str | None = Field(default=None, description="Project id", exclude=True)

    endpoint: str = Field(description="Endpoint for request")

    method: str = Field(description="HTTP method")

    content_type: str | None = Field(default=None, description="HTTP Content-Type")

    @field_validator("api_key", "openai_organization", "openai_project")
    @classmethod
    def get_id(cls, value: str) -> str:
        if api_key := getenv(value):
            return api_key
        else:
            return value

    def get_endpoint(self, path_param: OpenAIEndpointPathParam = None):
        if path_param is None:
            return self.endpoint
        else:
            return self.endpoint.format(**path_param.model_dump())

    @property
    def base_url(self):
        return "https://api.openai.com/v1/"

    async def invoke(self, json_data: OpenAIEndpointRequestBody = None,
                     params: OpenAIEndpointQueryParam = None,
                     form_data: OpenAIEndpointRequestBody = None,
                     path_param: OpenAIEndpointPathParam = None,
                     output_file: str = None):
        def get_headers():
            header = {"Authorization": f"Bearer {self.api_key}"}
            if self.content_type:
                header["Content-Type"] = self.content_type
            if self.openai_organization:
                header["OpenAI-Organization"] = self.openai_organization
            if self.openai_project:
                header["OpenAI-Project"] = self.openai_project
            return header

        def parse_form_data(data: OpenAIEndpointRequestBody):
            form_data = aiohttp.FormData()
            for field in data.model_fields:
                if value := getattr(data, field):
                    if isinstance(value, IOBase):
                        form_data.add_field(field, getattr(data, field))
                    else:
                        form_data.add_field(field, str(getattr(data, field)))
            return form_data

        url = self.base_url + self.get_endpoint(path_param)
        headers = get_headers()
        json_data = json_data.model_dump(exclude_unset=True) if json_data else None
        params = params.model_dump(exclude_unset=True) if params else None
        form_data = parse_form_data(form_data) if form_data else None

        async with aiohttp.ClientSession() as client:
            async with client.request(method=self.method, url=url, headers=headers, json=json_data, params=params, data=form_data) as response:
                response.raise_for_status()

                if output_file:
                    try:
                        with open(output_file, 'wb') as f:
                            f.write(await response.read())
                    except Exception as e:
                        raise ValueError(f"Invalid to output the response to {output_file}. Error:{e}")
                if self.endpoint != "audio/speech":
                    if response.headers.get("Content-Type") == "application/json":
                        response_headers = response.headers
                        response_body = await response.json()
                    else:
                        response_headers = response.headers
                        response_body = await response.text()

                    return response_body, response_headers

                else:
                    return None, response.headers   # audio has no response object

    def __repr__(self):
        return (f"OpenAIRequest(endpoint={self.endpoint}, method={self.method}, "
                f"content_type={self.content_type})")
