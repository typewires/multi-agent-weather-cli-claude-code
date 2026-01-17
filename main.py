import sys
import requests

from geocoding import get_coordinates
from weather import get_weather
from temperature import celsius_to_fahrenheit
from wind import ms_to_mph
from weather_codes import get_weather_description
from display import format_weather


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <city_name>")
        sys.exit(1)

    city_name = sys.argv[1]

    try:
        # Get coordinates for the city
        location = get_coordinates(city_name)

        # Get weather data
        weather_data = get_weather(location["latitude"], location["longitude"])

        # Convert units
        temp_c = weather_data["temperature"]
        temp_f = celsius_to_fahrenheit(temp_c)
        wind_ms = weather_data["windspeed"]
        wind_mph = ms_to_mph(wind_ms)

        # Get weather description
        description = get_weather_description(weather_data["weathercode"])

        # Format and print output
        output = format_weather(
            location["name"],
            temp_c,
            temp_f,
            description,
            wind_ms,
            wind_mph
        )
        print(output)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
