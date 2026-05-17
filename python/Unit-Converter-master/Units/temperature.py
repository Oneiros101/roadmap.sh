class Temperature:
    def __init__(self, value, from_unit, to_unit):
        self.__value = value
        self.__from_unit = from_unit.lower()
        self.__to_unit = to_unit.lower()

    measure_units = {"Celsius": "°C", "Kelvin": "°K", "Fahrenheit": "°F"}

    # Public dictionary to be accessed in app.py to display the temperature symbols
    __conversion_methods = {
        "celsius": {
            "kelvin": lambda v: float(v) + 273.15,
            "fahrenheit": lambda v: (float(v) * 9 / 5) + 32,
        },
        "kelvin": {
            "celsius": lambda v: float(v) - 273.15,
            "fahrenheit": lambda v: (float(v) - 273.15) * 5 / 9 + 32,
        },
        "fahrenheit": {
            "celsius": lambda v: (float(v) - 32) * 5 / 9,
            "kelvin": lambda v: (float(v) - 32) * 5 / 9 + 273.15,
        },
    }

    def convert_temperature(self):
        if self.__from_unit == self.__to_unit:
            return self.__value
        return self.__conversion_methods[self.__from_unit][self.__to_unit](self.__value)
