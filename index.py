import decimal
from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,SubmitField,DecimalField,IntegerField)
from wtforms.validators import DataRequired
from math import pow


app = Flask(__name__)
app.config['SECRET_KEY'] = 'izzasecret'


class SIP_Form(FlaskForm):
	name = StringField('Your name : ')
	monthly_investment = DecimalField('Your Monthly Investment')
	age = StringField('Age (Not to make you feel old) : ')
	virgin = BooleanField('Are you a virgin : ')
	expected_return_rate = StringField('Return Rate : ')
	time_period = StringField('Time Period : ')
	submit = SubmitField('Submit')

@app.route('/',methods = ['GET','POST'])
def index():
	form = SIP_Form()
	if form.validate_on_submit():
		session['name'] =  form.name.data + 'Chutiya hai' 
		session['age'] = float(form.age.data)
		session['monthly_investment'] = float(form.monthly_investment.data)
		session['time_period'] = float(form.time_period.data)
		session['expected_return_rate'] = float(form.expected_return_rate.data)
		monthly_rate_of_return = session['expected_return_rate']/1200
		n = session['time_period'] * 12
		session['maturity_value']=round((session['monthly_investment'] * (1+monthly_rate_of_return) * ((pow((1+monthly_rate_of_return),n)) - 1)/monthly_rate_of_return),2)


		return redirect(url_for('result'))
	return render_template('index.html',form = form)



@app.route('/result',methods = ['GET','POST'])
def result():
	return render_template('result.html')


if __name__ == '__main__':
	app.run(debug=True)






