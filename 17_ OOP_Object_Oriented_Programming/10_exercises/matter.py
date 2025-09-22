"""
Matter
In the previous two exercises, we created a Water and Mercury class. You probably noticed that we used the same exact
state method for both classes. However, repeated code is a bad practice and should be avoided. One way to avoid typing 
the state method more than once is to create a parent class from which both Water and Mercury inherit. That way you only 
have to write the state method in the parent class and Water and Mercury will have access to state since they will inherit 
the method from their parent. It makes sense to name the parent Matter since Water and Mercury are both matters.

Your exact task for this exercise is to create a Matter parent class, and a Water, and Mercury child class. Specifically, your tasks are:
1. Create a Matter class which has:
    1.1 An __init__ method with a self and temperature argument.
    1.2. A state method with a self argument. The method should behave exactly as it did in the previous exercises returning 'gas', 'liquid', or 'solid' depending on the value of temperature.
    1.3 A freezing_temperature and boiling_temperature class variable, both equal to None.
2. Create a Water and Mercury class which inherit from Matter and:
    2.1 Each class should have a freezing_temperature and boiling_temperature class variable equal to 0 and 100 for water, and -38.83 and 356.7 for mercury, respectively."""
    
class Matter:
    freezing_temperature = None
    boiling_temperature = None
    
    def __init__(self, temperature):
        self.temperature = temperature
        
    def state(self):
        if self.temperature <= self.__class__.freezing_temperature:
            return 'solid'
        elif self.__class__.freezing_temperature < self.temperature < self.__class__.boiling_temperature:
            return 'liquid'
        else:
            return 'gas'
        
"""Water
How about writing some more classes to practice OOP?
Your task for this exercise is to create a Water class that has these attributes:
Methods:
__init__
state
Class variables:
boiling_temperature equal to 100
freezing_temperature equal to 0
Instance variables:
temperature

The state method should return:
    The string 'solid' if temperature is less or equal to freezing_temperature.
    The string 'liquid' if temperature is higher than freezing_temperature and lower than boiling_temperature.
    The string 'gas' if temperature is higher than boiling_temperature"""


class Water(Matter):
    boiling_temperature = 100
    freezing_temperature = 0
    
    def __init__(self, temperature):
        super().__init__(temperature)


# Test the Water class
if __name__ == "__main__":
    # Test different states
    ice = Water(-10)
    water = Water(25)
    steam = Water(150)
    
    print(f"Water at -10°C is in {ice.state()} state")
    print(f"Water at 25°C is in {water.state()} state")  
    print(f"Water at 150°C is in {steam.state()} state")
    
    # Test boundary conditions
    freezing_point = Water(0)
    boiling_point = Water(100)
    
    print(f"Water at 0°C is in {freezing_point.state()} state")
    print(f"Water at 100°C is in {boiling_point.state()} state")
    
    
    """Mercury
Create a class like Water, but for mercury. Note that for mercury boiling_temperature is 356.7 and freezing_temperature is -38.83."""

class Mercury(Matter):
    boiling_temperature = 356.7
    freezing_temperature = -38.83

    def __init__(self, temperature):
        super().__init__(temperature)

# Test the Mercury class:
if __name__ == "__main__":
    # Test the different states
    ice = Mercury(-40)
    liquid = Mercury(0)
    gas = Mercury(400)

    print(f"Mercury at -40°C is in {ice.state()} state")
    print(f"Mercury at 0°C is in {liquid.state()} state")
    print(f"Mercury at 400°C is in {gas.state()} state")

    # Test boundary conditions:
    freezing_point = Mercury(-38.83)
    boiling_point = Mercury(356.7)

    print(f"Mercury at -38.83°C is in {freezing_point.state()} state")
    print(f"Mercury at 356.7°C is in {boiling_point.state()} state")
    
    # Test inheritance - both classes use the same state method from Matter
    print("\n--- Inheritance Test ---")
    print(f"Water instance uses state method from: {Water.state}")
    print(f"Mercury instance uses state method from: {Mercury.state}")
    print(f"Both inherit from Matter: {issubclass(Water, Matter)} and {issubclass(Mercury, Matter)}")
    
    
    
class Matter:
        boiling_temperature = None
        freezing_temperature = None

        def __init__(self, temperature):
            self.temperature = temperature

        def state(self):
            if self.temperature <= self.freezing_temperature:
                return 'solid'
            elif self.freezing_temperature < self.temperature < self.boiling_temperature:
                return 'liquid'
            else:
                return 'gas'


class Water(Matter):
        boiling_temperature = 100
        freezing_temperature = 0


class Mercury(Matter):
        boiling_temperature = 356.7
        freezing_temperature = -38.83