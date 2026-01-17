import requests


def get_weather(latitude, longitude):
    """
    Fetch current weather data for the given coordinates.

    Args:
        latitude: Latitude coordinate
        longitude: Longitude coordinate

    Returns:
        dict with 'temperature' (Celsius), 'windspeed' (m/s), and 'weathercode'
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    current = data["current_weather"]

    return {
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "weathercode": current["weathercode"]
    }
