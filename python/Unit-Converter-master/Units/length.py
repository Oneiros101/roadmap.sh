class Length:
    def __init__(self, value, from_unit, to_unit):
        self.__value = value
        self.__from_unit = from_unit.lower()
        self.__to_unit = to_unit.lower()

    # Public dictionary to be accessed in app.py to display the metric symbols
    measure_units = {
        "Centimeter": "cm",
        "Meter": "m",
        "Kilometer": "km",
        "Foot": "ft",
        "Inch": "in",
        "Yard": "yd",
        "Mile": "mile",
    }

    # Conversion factors from base unit (meters)
    # All units are converted to meters
    __conversion_factors = {
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "foot": 0.3048,
        "inch": 0.0254,
        "yard": 0.9144,
        "mile": 1609.34,
    }

    def convert_length(self):
        # Convert value to meters first
        value_in_meter = (
            float(self.__value) * self.__conversion_factors[self.__from_unit]
        )
        # Then, convert it to target unit
        return value_in_meter / self.__conversion_factors[self.__to_unit]
