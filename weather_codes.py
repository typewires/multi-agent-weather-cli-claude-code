def get_weather_description(code):
    """
    Map WMO weather code to human-readable description.

    Args:
        code: WMO weather code

    Returns:
        str: Human-readable weather description
    """
    if code == 0:
        return "Clear sky"
    elif code in (1, 2, 3):
        return "Partly cloudy"
    elif code in (45, 46, 47, 48):
        return "Fog"
    elif code in (51, 52, 53, 54, 55):
        return "Drizzle"
    elif code in (61, 62, 63, 64, 65):
        return "Rain"
    elif code in (71, 72, 73, 74, 75):
        return "Snow"
    elif code in (80, 81, 82):
        return "Rain showers"
    elif code in (95, 96, 97, 98, 99):
        return "Thunderstorm"
    else:
        return "Unknown"
