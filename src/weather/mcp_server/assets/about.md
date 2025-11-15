# About Weather Agent

This agent uses the Weather Forecast API (<https://open-meteo.com/>).  
Weather Forecast provides seamless integration of high-resolution weather models with up 16 days forecast.

## Usage

### Tools

#### Get Weather Forecast

The tool `get_forecast` retrieves the weather forecast for a given location.  
The location is provided through latitude and longitude coordinates.

The output contains multiple lines, with each time the following information:

- Time: the hour of the forecast.
- Temperature: the temperature in Celsius degrees.
- Rain: the rain in millimeters.
- Wind: the wind in kilometers per hour.

Sample line:

```raw
Time: 2025-11-22 10:00 - Temperature: 13.6°C, Rain: 0.0mm, Wind: 15.1km/h
```

#### Get Favorite Cities

The tool `get_favorite_cities` returns a list of favorites cities.

It can be used to get the weather forecast of some cities.

### Prompts

| Prompt                         | Description                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `get_weather_prompt`           | Generates a prompt to get the weather of a given city.                              |
| `get_demonstration_prompt`     | Generates a demonstration prompt to get the weather of a city.                      |
| `get_weather_advice_prompt`    | Generates an advice prompt based on the weather of a city.                          |
| `get_favorite_cities_prompt`   | Generates a prompt to get the weather of my favorite cities.                        |
| `get_where_should_i_go_prompt` | Generates a prompt to indicate where I should move based on the weather conditions. |

### Resources

The resource `resource://about` provides access to this document.
