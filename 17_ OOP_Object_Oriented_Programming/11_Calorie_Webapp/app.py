from temperature import Temperature
from calorie import Calorie
from flask import Flask, request, render_template
from flask.views import MethodView
from wtforms import Form, FloatField, IntegerField, validators, StringField, SubmitField

app = Flask(__name__)


class CalorieForm(Form):
    weight = FloatField('Weight (kg)', [validators.NumberRange(min=1, max=300, message="Weight must be between 1-300 kg")], default=63.0)
    height = FloatField('Height (cm)', [validators.NumberRange(min=50, max=250, message="Height must be between 50-250 cm")], default=173.0)
    age = IntegerField('Age (years)', [validators.NumberRange(min=1, max=120, message="Age must be between 1-120 years")], default=39)
    country = StringField('Country', [validators.DataRequired(message="Country is required")], default="romania")
    city = StringField('City', [validators.DataRequired(message="City is required")], default="bucharest")
    button = SubmitField('Calculate Calories')


class Homepage(MethodView):
    
    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):
    
    def get(self):
        calories_form = CalorieForm()
        return render_template("calories_form_page.html", calories_form=calories_form)

    def post(self):
        calories_form = CalorieForm(request.form)
        if calories_form.validate():
            weight = calories_form.weight.data
            height = calories_form.height.data
            age = calories_form.age.data
            country = calories_form.country.data
            city = calories_form.city.data
            
            temperature = Temperature(country, city).get()
            if temperature is None:
                return render_template("calories_form_page.html", calories_form=calories_form, 
                result=False, error="Could not fetch temperature. Please check the country and city names.")
            
            calorie = Calorie(weight=weight, height=height, age=age, temperature=temperature)
            calories = calorie.calculate_bmr()
            return render_template("calories_form_page.html", calories_form=calories_form, 
            result=True, calories=round(calories, 2))
        
        return render_template("calories_form_page.html", calories_form=calories_form, 
        result=False, error="Please correct the form errors.")


app.add_url_rule("/", view_func=Homepage.as_view("homepage"))
app.add_url_rule("/calories_form", view_func=CaloriesFormPage.as_view("calories_form_page"))

if __name__ == "__main__":
    app.run(debug=True)

