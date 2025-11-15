from dataclasses import dataclass
from datetime import datetime


@dataclass
class WeatherPrediction:
    """Weather Prediction Entry."""

    hour: datetime
    temperature: float
    rain: float
    wind: float
