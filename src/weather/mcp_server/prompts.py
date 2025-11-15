from fastmcp.prompts import PromptMessage
from mcp.types import TextContent

from mcp_server.server import mcp


def __get_weather_prompt(city: str) -> PromptMessage:
    content = f'What is the weather in {city}?'
    return PromptMessage(
        role='user',
        content=TextContent(type='text', text=content),
    )


@mcp.prompt()
async def get_weather_prompt(city: str) -> PromptMessage:
    """
    Generates a prompt to get the weather of a given city.

    Args:
        city (str): The city to request the weather for.
    """
    return __get_weather_prompt(city)


@mcp.prompt()
async def get_demonstration_prompt() -> PromptMessage:
    """Generates a demonstration prompt to get the weather of a city."""
    return __get_weather_prompt('Redmond')


@mcp.prompt()
async def get_weather_advice_prompt(city: str) -> PromptMessage:
    """
    Generates an advice prompt based on the weather of a city.

    Args:
        city (str): The city to request the weather advice for.
    """
    content = f'Should I take an umbrella to go out in {city}?'
    return PromptMessage(
        role='user',
        content=TextContent(type='text', text=content),
    )


@mcp.prompt()
async def get_favorite_cities_prompt() -> PromptMessage:
    """Generates a prompt to get the weather of my favorite cities."""
    content = 'What is the weather in my favorite cities?'
    return PromptMessage(
        role='user',
        content=TextContent(type='text', text=content),
    )


@mcp.prompt()
async def get_where_should_i_go_prompt() -> PromptMessage:
    """Generates a prompt to indicate where I should move based on the weather conditions."""
    content = 'In which of my favorite cities should I go to benefit from the warmest weather?'
    return PromptMessage(
        role='user',
        content=TextContent(type='text', text=content),
    )
