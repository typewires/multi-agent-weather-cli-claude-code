def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit, rounded to 1 decimal place
    """
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 1)
