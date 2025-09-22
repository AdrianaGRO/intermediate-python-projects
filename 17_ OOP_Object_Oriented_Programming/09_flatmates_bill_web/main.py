from flask.views import MethodView
from wtforms import Form, StringField, validators
from flask import Flask, render_template, request 


app = Flask(__name__)

class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', form=bill_form)

class ResultsPage(MethodView):
    def get(self):
        return render_template('results.html')
    
    def post(self):
        amount = float(request.form.get('amount', 0))
        name1 = request.form.get('name1')
        days_in_house1 = int(request.form.get('days_in_house1', 0))
        name2 = request.form.get('name2')
        days_in_house2 = int(request.form.get('days_in_house2', 0))
        # Calculate shares
        total_days = days_in_house1 + days_in_house2
        if total_days > 0:
            amount1 = round(amount * days_in_house1 / total_days, 2)
            amount2 = round(amount * days_in_house2 / total_days, 2)
        else:
            amount1 = amount2 = None
        return render_template('results.html', name1=name1, amount1=amount1, name2=name2, amount2=amount2)
    

class BillForm(Form):
    name = StringField('Name', [validators.InputRequired()])
    amount = StringField('Amount', [validators.InputRequired()])


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))


if __name__ == "__main__":
    app.run(debug=True)