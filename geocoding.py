import requests


def get_coordinates(city_name):
    """Get coordinates for a city using the Open-Meteo geocoding API.

    Args:
        city_name: Name of the city to look up.

    Returns:
        A dict with 'latitude', 'longitude', and 'name' (full city name).

    Raises:
        ValueError: If the city is not found.
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        raise ValueError(f"City not found: {city_name}")

    result = data["results"][0]
    return {
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "name": result["name"]
    }
