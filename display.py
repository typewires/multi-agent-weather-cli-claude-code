def format_weather(city_name, temp_c, temp_f, description, wind_ms, wind_mph):
    """
    Format weather information into a readable multi-line string.

    Args:
        city_name: Name of the city
        temp_c: Temperature in Celsius
        temp_f: Temperature in Fahrenheit
        description: Weather description
        wind_ms: Wind speed in meters per second
        wind_mph: Wind speed in miles per hour

    Returns:
        str: Formatted multi-line weather report
    """
    return f"""Weather for {city_name}
---------------------------
Condition: {description}
Temperature: {temp_c}°C / {temp_f}°F
Wind Speed: {wind_ms} m/s / {wind_mph} mph"""
