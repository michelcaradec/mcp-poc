from typing import List

from model import WeatherPrediction

__LIST_SEPARATOR = '\n---\n'
__DATETIME_FORMAT = r'%Y-%m-%d %H:%M'


def format_forecast(forecasts: List[WeatherPrediction]) -> str:
    """
    Format a weather forecast for LLM ingestion.

    Args:
        forecasts (List[WeatherPrediction]): the weather forecast to format.
    """
    return __LIST_SEPARATOR.join(
        [
            f'Time: {f.hour:{__DATETIME_FORMAT}} - Temperature: {f.temperature}°C, Rain: {f.rain}mm, Wind: {f.wind}km/h'
            for f in forecasts
        ]
    )
