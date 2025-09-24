class Calorie:
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate_bmr(self):
        # Basic BMR calculation using Mifflin-St Jeor Equation
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        return bmr
    
    def get_kj(self):
        return self.calculate_bmr() * 4.184
    
    def kj_to_kcal(self, kj):
        """Convert kilojoules to kilocalories."""
        filepath = "/Users/adricati/Personal Development/intermediate-python-projects/17_ OOP_Object_Oriented_Programming/10_exercises/calorie_to_kcal.txt"
        kj = self.get_kj()
        with open(filepath, "w") as file: file.write(str(self.get_kj()))
    
calorie = Calorie(weight=63, height=173, age=49, temperature=22)
calorie = calorie.kj_to_kcal(calorie.get_kj())
print("GIT")