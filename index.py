# Importing necessary methods and modules

import decimal
from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,SubmitField,DecimalField,RadioField)
from wtforms.validators import DataRequired
from math import pow


#Initializing Flask application 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'izzasecret'


#Form Class for choosing the calculator
class calculator_choice(FlaskForm):
	calculator = RadioField('SIP OR LUMPSUM', choices=[('lumpsum','lumpsum'),('sip','sip')])
	submit = SubmitField('submit')

#Form class for SIP Calculator
class SIP_Form(FlaskForm):
	monthly_investment = DecimalField('Your Monthly Investment')
	expected_return_rate = StringField('Return Rate : ')
	time_period = StringField('Time Period : ')
	submit = SubmitField('Submit')

#Form class for LUMPSUM calculator
class LUMPSUM_Form(FlaskForm):
	investment = StringField('Total Investment')
	expected_return_rate = StringField('Return Rate : ')
	time_period = StringField('Time period : ')
	submit = SubmitField('submit')



#Method for HomePage

@app.route('/',methods = ['GET','POST'])
def index():
	choosen = calculator_choice()
	print('index() being executed')
	if choosen.validate_on_submit():
		print('Form submitted')
		session['calculator'] = choosen.calculator.data
		if(session['calculator'] == 'lumpsum'):
			return redirect(url_for('lumpsum'))
		elif(session['calculator'] == 'sip'):
			return redirect(url_for('sip'))
	else:
		print("Oooooopsy!")
	return render_template('index.html',choosen = choosen)



#Method for SIP Calculator Page

@app.route('/SIP',methods = ['GET','POST'])
def sip():
	
	form = SIP_Form()
	if form.validate_on_submit():
		session['monthly_investment'] = float(form.monthly_investment.data)
		session['time_period'] = float(form.time_period.data)
		session['expected_return_rate'] = float(form.expected_return_rate.data)
		monthly_rate_of_return = session['expected_return_rate']/1200
		n = session['time_period'] * 12
		session['maturity_value']=round((session['monthly_investment'] * (1+monthly_rate_of_return) * ((pow((1+monthly_rate_of_return),n)) - 1)/monthly_rate_of_return),2)


		return redirect(url_for('result'))
	return render_template('SIP.html',form = form)



#Method For Lumpsum calculator page

@app.route('/lumpsum',methods = ['GET','POST'])
def lumpsum():
	form = LUMPSUM_Form()
	if form.validate_on_submit():
		session['in']
	return render_template('LUMPSUM.html')



#Method for result page

@app.route('/result',methods = ['GET','POST'])
def result():
	return render_template('result.html')


if __name__ == '__main__':
	app.run(debug=True)






