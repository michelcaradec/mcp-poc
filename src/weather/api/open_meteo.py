from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Optional,
)

import httpx

from model import WeatherPrediction

__OPEN_METEO_API_BASE = 'https://api.open-meteo.com'
__USER_AGENT = 'weather-app/1.0'
__DATETIME_API_FORMAT = r'%Y-%m-%dT%H:%M'


async def __make_request(
    url: str,
    params: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    headers = {
        'User-Agent': __USER_AGENT,
        'Accept': 'application/json',
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url,
                params=params,
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            return response.json()
        except Exception:
            return None


async def get_forecast(
    latitude: float,
    longitude: float,
) -> Optional[List[WeatherPrediction]]:
    """
    Get weather forecast for a location.

    Args:
        latitude: Latitude of the location.
        longitude: Longitude of the location.
    """
    # Sample request:
    # https://api.open-meteo.com/v1/forecast?latitude=48.11087&longitude=-1.68005&hourly=temperature_2m,rain,wind_speed_10m&forecast_days=1
    url = f'{__OPEN_METEO_API_BASE}/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': [
            'temperature_2m',
            'rain',
            'wind_speed_10m',
        ],
        'forecast_days': 1,
    }

    weather = await __make_request(url, params)
    if not weather:
        return None

    hourly = weather['hourly']
    forecasts: List[WeatherPrediction] = []
    for time, temperature, rain, wind in zip(
        hourly['time'],
        hourly['temperature_2m'],
        hourly['rain'],
        hourly['wind_speed_10m'],
    ):
        forecasts.append(
            WeatherPrediction(
                datetime.strptime(time, __DATETIME_API_FORMAT),
                float(temperature),
                float(rain),
                float(wind),
            )
        )

    return forecasts
