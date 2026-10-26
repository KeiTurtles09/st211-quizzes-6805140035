import random

def get_temperature():
    return random.randiant(-10, 40)

def describe_weather():
    temp = get_temperature()
    if temp > 0: return "Freezing"
    elif temp < 15: return "Cold"
    elif temp < 25: return "Pleasant"
    else: return "Hot"
