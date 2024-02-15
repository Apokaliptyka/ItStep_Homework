class CelsiusTemperatureSensor:
    def set_temperature(self, temperature: float):
        self._temperature = temperature

    def get_temperature_celsius(self) -> float:
        return self._temperature


class FahrenheitTemperatureSensor:

    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature: float):
        self._temperature = temperature

    def get_temperature_fahrenheit(self) -> float:
        return self._temperature


class TemperatureSensorAdapter:
    def __init__(self, fahr_obj: FahrenheitTemperatureSensor):
        self._fahr_obj = fahr_obj

    def set_temperature(self, temperature: float):
        self._fahr_obj.set_temperature((temperature - 32) / 1.8)

    def get_temperature_celsius(self) -> float:
        return self._fahr_obj.get_temperature_fahrenheit()


def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")


if __name__ == "__main__":
    fahrenheit_sensor = FahrenheitTemperatureSensor()
    cels_sensor = CelsiusTemperatureSensor()

    adapter = TemperatureSensorAdapter(fahrenheit_sensor)

    adapter.set_temperature(80)
    cels_sensor.set_temperature(35)

    display_temperature(adapter)
    display_temperature(cels_sensor)
