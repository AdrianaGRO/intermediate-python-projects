from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

from models.flat import Bill, Flatmate
from models.reports import PdfReport, FileSharer

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'


class BillForm(FlaskForm):
    """Form for bill sharing input"""
    amount = FloatField('Bill Amount ($): ', validators=[DataRequired(), NumberRange(min=0.01)], default=500)
    period = StringField('Bill Period (e.g., September 2025): ', validators=[DataRequired()], default="September 2025")
    
    name1 = StringField('First Flatmate Name: ', validators=[DataRequired()], default="Antonio")
    days_in_house1 = IntegerField('Days in house: ', validators=[DataRequired(), NumberRange(min=1, max=31)], default=20)

    name2 = StringField('Second Flatmate Name: ', validators=[DataRequired()], default="Adriana")
    days_in_house2 = IntegerField('Days in house: ', validators=[DataRequired(), NumberRange(min=1, max=31)], default=15)

    submit = SubmitField('Calculate')


@app.route('/')
def index():
    """Home page with form"""
    bill_form = BillForm()
    return render_template('bill_form_page.html', billform=bill_form)


@app.route('/results', methods=['POST'])
def results():
    """Process form and show results"""
    bill_form = BillForm()
    
    if bill_form.validate_on_submit():
        # Create objects from form data
        the_bill = Bill(amount=bill_form.amount.data, period=bill_form.period.data)
        flatmate1 = Flatmate(name=bill_form.name1.data, days_in_house=bill_form.days_in_house1.data)
        flatmate2 = Flatmate(name=bill_form.name2.data, days_in_house=bill_form.days_in_house2.data)
        
        # Calculate payments
        flatmate1_pay = round(flatmate1.pays(the_bill, flatmate2), 2)
        flatmate2_pay = round(flatmate2.pays(the_bill, flatmate1), 2)
        
        # Generate PDF report
        pdf_report = PdfReport(filename=f"{the_bill.period.replace(' ', '_')}_bill.pdf")
        pdf_file_path = pdf_report.generate(flatmate1, flatmate2, the_bill)
        
        # Try to share file
        file_sharer = FileSharer(filepath=pdf_file_path)
        file_url = file_sharer.share()
        
        return render_template('results.html',
                             flatmate1=flatmate1,
                             flatmate2=flatmate2,
                             flatmate1_pay=flatmate1_pay,
                             flatmate2_pay=flatmate2_pay,
                             file_url=file_url)
    else:
        # Form validation failed, return to form with errors
        return render_template('bill_form_page.html', billform=bill_form)


if __name__ == '__main__':
    app.run(debug=True)