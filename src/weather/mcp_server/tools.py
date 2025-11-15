from typing import List

from fastmcp import Context

from utils import format_forecast
from mcp_server.server import mcp
from api.open_meteo import (
    get_forecast as get_open_meteo_forecast,
)


@mcp.tool()
async def get_forecast(
    latitude: float,
    longitude: float,
    ctx: Context,
) -> str:
    """
    Get the weather forecast for a location.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        ctx (Context): The context of the client.
            See https://fastmcp.wiki/en/servers/context.
    """
    # The logs can be seen in the file ~/.config/Claude/logs/mcp-server-weather.log
    # Logs with the minimum level "info" will appear in the console where the MCP server was started.
    await ctx.info(f'Get weather forecast for ({latitude=}, {longitude=})')
    await ctx.debug(f'client_id: {ctx.client_id}')
    await ctx.debug(f'request_id: {ctx.request_id}')

    await ctx.report_progress(0, 100, 'Starting')

    forecasts = await get_open_meteo_forecast(latitude, longitude)

    await ctx.report_progress(100, 100, 'Completed')

    if not forecasts:
        await ctx.error(f'Get weather forecast error for ({latitude=}, {longitude=})')

        return 'Unable to fetch forecast data for this location.'

    return format_forecast(forecasts)


@mcp.tool()
async def get_favorite_cities() -> List[str]:
    """Get a list of favorite cities."""
    return [
        'Rennes',
        'Brest',
        'Bonneval-sur-Arc',
        'Heraklion',
    ]
