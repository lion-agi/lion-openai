from unittest.mock import AsyncMock, patch

import pytest

from lion_openai.chat_completions.request.request_body import (
    OpenAIChatCompletionRequestBody,
)
from lion_openai.chat_completions.response.response_body import (
    OpenAIChatCompletionResponseBody,
)
from lion_openai.client import OpenAIClient
from lion_openai.embeddings.request.request_body import OpenAIEmbeddingRequestBody
from lion_openai.embeddings.response.response_body import OpenAIEmbeddingResponseBody


@pytest.fixture
def openai_client():
    return OpenAIClient(api_key="test_api_key")


@pytest.mark.asyncio
async def test_chat_completion(openai_client):
    mock_response = OpenAIChatCompletionResponseBody(
        id="chatcmpl-123",
        object="chat.completion",
        created=1677652288,
        model="gpt-3.5-turbo-0613",
        system_fingerprint="fp_44709d6fcb",
        choices=[
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Hello! How can I assist you today?",
                },
                "finish_reason": "stop",
            }
        ],
        usage={"prompt_tokens": 9, "completion_tokens": 12, "total_tokens": 21},
    )

    with patch.object(
        openai_client, "_make_request", new_callable=AsyncMock
    ) as mock_request:
        mock_request.return_value = mock_response

        request = OpenAIChatCompletionRequestBody(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello!"}]
        )

        response = await openai_client.chat_completion(request)

        assert response.id == "chatcmpl-123"
        assert (
            response.choices[0].message.content == "Hello! How can I assist you today?"
        )
        assert response.usage.total_tokens == 21


@pytest.mark.asyncio
async def test_embedding(openai_client):
    mock_response = OpenAIEmbeddingResponseBody(
        object="list",
        data=[
            {
                "object": "embedding",
                "embedding": [0.0023064255, -0.009327292, -0.0028842222],
                "index": 0,
            }
        ],
        model="text-embedding-ada-002",
        usage={"prompt_tokens": 8, "total_tokens": 8},
    )

    with patch.object(
        openai_client, "_make_request", new_callable=AsyncMock
    ) as mock_request:
        mock_request.return_value = mock_response

        request = OpenAIEmbeddingRequestBody(
            model="text-embedding-ada-002", input="Hello, world!"
        )

        response = await openai_client.embedding(request)

        assert response.object == "list"
        assert len(response.data) == 1
        assert len(response.data[0].embedding) == 3
        assert response.usage.prompt_tokens == 8


@pytest.mark.asyncio
async def test_chat_completion_error_handling(openai_client):
    with patch.object(
        openai_client, "_make_request", new_callable=AsyncMock
    ) as mock_request:
        mock_request.side_effect = Exception("API Error")

        request = OpenAIChatCompletionRequestBody(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello!"}]
        )

        with pytest.raises(Exception, match="API Error"):
            await openai_client.chat_completion(request)


# filepath: tests/test_openai_client.py
