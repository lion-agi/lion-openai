# lion-openai

## Description

An asynchronous Python package for interacting with the Lion system API.

## Project Structure

```
lion-openai/
├── lion_openai/
│   ├── __init__.py
│   ├── api.py
│   └── models.py
├── tests/
│   └── __init__.py
├── pyproject.toml
└── README.md
```

## Dependencies

- aiohttp: ^3.8.1
- pydantic: ^2.0.0

## Development Dependencies

- pytest: ^7.0
- pytest-asyncio: ^0.21.0
- black: ^22.3
- flake8: ^4.0
- isort: ^5.10

## Installation

To install the package, run:

```bash
poetry install
```

## Usage

Here is a simple asynchronous usage example:

```python
import asyncio
from lion_openai import LionAPI

async def main():
    api_key = "your_api_key"
    api = LionAPI(api_key)
    response = await api.make_request("GET", "https://api.example.com/data")
    print(response)

asyncio.run(main())
```

## Author

[Your Name] your.email@example.com

## License

MIT
