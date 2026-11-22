import random


def read_temperature():
    """Return temperature in Celsius (stub until the real sensor is connected)."""
    return round(random.uniform(20.0, 26.0), 1)


def read_humidity():
    """Return relative humidity in percent (stub)."""
    return round(random.uniform(35.0, 60.0), 1)


def read_co2():
    """Return CO2 concentration in ppm (stub)."""
    return random.randint(400, 1500)


def read_all():
    return {
        "temperature": read_temperature(),
        "humidity": read_humidity(),
        "co2": read_co2(),
    }
