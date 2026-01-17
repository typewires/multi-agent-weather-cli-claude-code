def ms_to_mph(meters_per_second):
    """
    Convert wind speed from meters per second to miles per hour.

    Args:
        meters_per_second: Wind speed in m/s

    Returns:
        float: Wind speed in mph, rounded to 1 decimal place
    """
    mph = meters_per_second * 2.237
    return round(mph, 1)
