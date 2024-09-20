import aiohttp
import asyncio
import logging
from typing import Any, Dict, Optional
from pydantic import BaseModel, ValidationError
from aiohttp import ClientSession, ClientResponseError
from tenacity import retry, stop_after_attempt, wait_exponential

class LionAPI:
    """
    A class to interact with the Lion system API asynchronously.
    """

    def __init__(self, api_key: str):
        """
        Initialize the LionAPI class with the provided API key.

        :param api_key: The API key to authenticate with the Lion system API.
        """
        self.api_key = api_key
        self.base_url = "https://api.example.com"
        self.session: Optional[ClientSession] = None
        self.logger = logging.getLogger(__name__)

    async def __aenter__(self):
        self.session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.session:
            await self.session.close()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def _make_request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make an asynchronous request to the Lion system API.

        :param method: The HTTP method (e.g., 'GET', 'POST').
        :param endpoint: The API endpoint to request.
        :param data: Optional data to include in the request.
        :return: The JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        if not self.session:
            self.session = ClientSession()

        try:
            async with self.session.request(method, url, json=data, headers=headers) as response:
                response.raise_for_status()
                return await response.json()
        except ClientResponseError as e:
            self.logger.error(f"API request failed with status code {e.status}")
            raise
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            raise

    async def get_data(self, endpoint: str) -> Dict[str, Any]:
        """
        Get data from the Lion system API.

        :param endpoint: The API endpoint to request.
        :return: The JSON response from the API.
        """
        return await self._make_request("GET", endpoint)

    async def post_data(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Post data to the Lion system API.

        :param endpoint: The API endpoint to request.
        :param data: The data to include in the request.
        :return: The JSON response from the API.
        """
        return await self._make_request("POST", endpoint, data)
