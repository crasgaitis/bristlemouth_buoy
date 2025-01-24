# utility functions/classes

class TempSensor:
    def __init__(self):
        self._temperature = 0 

    @property
    def value(self):
        """Getter method for temperature value."""
        return self._temperature

    @value.setter
    def value(self, new_value):
        """Setter method for temperature value."""
        self._temperature = new_value
        
    def to_fahrenheit(self):
        """Convert the current temperature to Fahrenheit."""
        if not isinstance(self._temperature, (int, float)):
            raise ValueError("Temperature must be a number.")
        fahrenheit = (self._temperature * 9/5) + 32
        return fahrenheit
        
    def from_fahrenheit(self):
        """Convert a given Fahrenheit temperature to Celsius."""
        if not isinstance(self._temperature, (int, float)):
            raise ValueError("Temperature must be a number.")
        celsius = (self._temperature - 32) * 5/9
        return celsius