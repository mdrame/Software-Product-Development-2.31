# by Kami Bigdely
# Docstrings and blank lines


class OnBoardTemperatureSensor:
    """Represents the CarbonMonoxide class's on board temperature sensor."""
    VOLTAGE_TO_TEMP_FACTOR = 5.6


    def __init__(self):
        pass


    def read_voltage(self):        
        """Returns the current voltage."""
        return 2.7


    def get_temperature(self):
        """
        Returns the current voltage multiplied by the on board 
        temperature sensor's volatage to temperature factor.
        """
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
  
class CarbonMonoxideSensor:
    """Represents the CarbonMonoxideDevice class's sensor."""
    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()


    def get_carbon_monoxide_level(self):
        """
        Returns the carbon monoxide level by using the convert_voltage_to_carbon_monoxide_level
        with the sensor's voltage and on board temp sensor's temperature.
        """
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide


    def read_sensor_voltage(self):
        # In real life, it should read from hardware.     
        """Returns the sensor's voltage."""   
        return 2.3


    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        """Returns the voltage multiplied by the CMSensor's voltage to co factor."""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    

class DisplayUnit:
    """Represents the CarbonMonoxideDevice class's display unit."""
    def __init__(self):
        self.string = ''


    def display(self, msg):
        """Prints the message given to the display unit."""
        print(msg)


class CarbonMonoxideDevice():
    """Represents the CarbonMonoxideDevice clas."""
    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit       
    
    
    def Display(self):
        """Sends a messege as a parameter for the DisplayUnit class's display function."""
        msg = 'Carbon Monoxide Level is : ' +  str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
    