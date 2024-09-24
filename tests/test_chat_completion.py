import asyncio
from unittest.mock import AsyncMock

import pytest


# Mock the OpenAIService and related classes
class MockOpenAIService:
    def create_chat_completion(self, model):
        return AsyncMock()


class MockSystemMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content


class MockUserMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content


class MockOpenAIChatCompletionRequestBody:
    def __init__(self, model, messages):
        self.model = model
        self.messages = messages


# The function we're testing
async def create_chat_completion(model: str, messages: list):
    request_body = MockOpenAIChatCompletionRequestBody(model=model, messages=messages)
    model_mock = openai.create_chat_completion(model=model)
    response = await model_mock.invoke(request_body)
    return response


# Global mock for OpenAIService
openai = MockOpenAIService()


@pytest.mark.asyncio
async def test_create_chat_completion():
    # Arrange
    model = "gpt-4o-mini"
    mes1 = MockSystemMessage(role="system", content="You are a helpful assistant.")
    mes2 = MockUserMessage(role="user", content="Hello!")
    messages = [mes1, mes2]

    mock_response = {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677858242,
        "model": "gpt-4o-mini",
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Hello! How can I assist you today?",
                },
                "finish_reason": "stop",
                "index": 0,
            }
        ],
    }

    # Set up the mock
    openai.create_chat_completion(model).invoke.return_value = mock_response

    # Act
    response = await create_chat_completion(model, messages)

    # Assert
    assert response == mock_response
    openai.create_chat_completion.assert_called_once_with(model=model)
    openai.create_chat_completion(model).invoke.assert_called_once()


# Run the test
if __name__ == "__main__":
    asyncio.run(test_create_chat_completion())
    print("Test completed successfully!")

# filepath: tests/test_chat_completion.py
