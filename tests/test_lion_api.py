import pytest
from lion_openai import LionAPI

@pytest.mark.asyncio
async def test_lion_api():
    api = LionAPI("test-key")
    result = await api.some_method()
    assert result == expected_result
