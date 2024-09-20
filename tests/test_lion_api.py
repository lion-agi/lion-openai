import pytest
from lion_openai import LionAPI

@pytest.mark.asyncio
async def test_get_data():
    api = LionAPI("test-key")
    result = await api.get_data("test-endpoint")
    assert result == {"key": "value"}

@pytest.mark.asyncio
async def test_post_data():
    api = LionAPI("test-key")
    data = {"key": "value"}
    result = await api.post_data("test-endpoint", data)
    assert result == {"key": "value"}

@pytest.mark.asyncio
async def test_error_handling():
    api = LionAPI("test-key")
    with pytest.raises(Exception):
        await api.get_data("invalid-endpoint")
