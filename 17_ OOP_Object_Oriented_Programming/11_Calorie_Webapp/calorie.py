
from temperature import Temperature



class Calorie:
    """Represents a calorie entry with food name and calorie amount. BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature"""
    
    def __init__ (self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
        
    def calculate_bmr(self):
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * self.temperature
        return bmr
    
if __name__ == "__main__":
    temperature = Temperature("italy", "rome").get()
    calorie = Calorie(weight=63, height=173, age=39, temperature=temperature)
    print(f"Calorie value: {calorie.calculate_bmr()}")
    