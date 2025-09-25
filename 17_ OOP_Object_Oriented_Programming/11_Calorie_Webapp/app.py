from temperature import Temperature
from calorie import Calorie
from flask import Flask, request, render_template
from flask.views import MethodView
from wtforms import Form, FloatField, IntegerField, validators, StringField, SubmitField, SelectField

app = Flask(__name__)


class CalorieForm(Form):
    weight = FloatField('Weight (kg)', [validators.NumberRange(min=1, max=300, message="Weight must be between 1-300 kg")], default=63.0)
    height = FloatField('Height (cm)', [validators.NumberRange(min=50, max=250, message="Height must be between 50-250 cm")], default=173.0)
    age = IntegerField('Age (years)', [validators.NumberRange(min=1, max=120, message="Age must be between 1-120 years")], default=39)
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], default='female')
    activity_level = SelectField('Activity Level', choices=[
        ('sedentary', 'Sedentary'),
        ('lightly active', 'Lightly Active'),
        ('moderately active', 'Moderately Active'),
        ('very active', 'Very Active'),
        ('super active', 'Super Active')
    ], default='moderately active')
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
            gender = calories_form.gender.data
            activity_level = calories_form.activity_level.data
            
            calorie = Calorie(weight=weight, height=height, age=age, gender=gender, activity_level=activity_level)
            bmr = calorie.calculate_bmr()
            tdee = calorie.calculate_tdee()
            return render_template("calories_form_page.html", calories_form=calories_form, 
            result=True, bmr=round(bmr, 2), tdee=round(tdee, 2))
        
        return render_template("calories_form_page.html", calories_form=calories_form, 
        result=False, error="Please correct the form errors.")


app.add_url_rule("/", view_func=Homepage.as_view("homepage"))
app.add_url_rule("/calories_form", view_func=CaloriesFormPage.as_view("calories_form_page"))

if __name__ == "__main__":
    app.run(debug=True)

