
from temperature import Temperature



class Calorie:
    """
    Represents a calorie entry and calculates BMR and TDEE using the Mifflin-St Jeor equation.
    For Men:    BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) + 5
    For Women:  BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) - 161
    """

    ACTIVITY_FACTORS = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "super active": 1.9
    }

    def __init__(self, weight, height, age, gender, activity_level):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender.lower()
        self.activity_level = activity_level.lower()

    def calculate_bmr(self):
        if self.gender == "male":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.gender == "female":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        else:
            raise ValueError("Gender must be 'male' or 'female'.")
        return bmr

    def calculate_tdee(self):
        bmr = self.calculate_bmr()
        factor = self.ACTIVITY_FACTORS.get(self.activity_level)
        if factor is None:
            raise ValueError(f"Invalid activity level: {self.activity_level}")
        return bmr * factor
    
if __name__ == "__main__":
    # Example usage
    calorie = Calorie(weight=63, height=173, age=39, gender="female", activity_level="moderately active")
    print(f"BMR: {calorie.calculate_bmr():.2f}")
    print(f"TDEE: {calorie.calculate_tdee():.2f}")
    