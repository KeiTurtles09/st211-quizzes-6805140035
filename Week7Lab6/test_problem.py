from weather import decribe_weather

def test_weather_description():
    result = decribe_weather()
    assert result in ["Freezing", "Cold", "Pleasant", "Hot"]