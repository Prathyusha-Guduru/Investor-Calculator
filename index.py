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


#Global values for choice
choice = ''

#Form Class for choosing the calculator
class calculator_choice(FlaskForm):
	calculator = RadioField('Choose the Calculator', choices=[('lumpsum','lumpsum'),('sip','sip'),('fd','fd')])
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

#Form class for FD calculator
class FD_Form(FlaskForm):
	investment = StringField('Total Investment')
	rate_of_interest = StringField('Return Rate : ')
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
		global choice
		if(session['calculator'] == 'lumpsum'):
			choice = 'lumpsum'
			return redirect(url_for('lumpsum'))
		elif(session['calculator'] == 'sip'):
			choice = 'sip'
			return redirect(url_for('sip'))
		elif(session['calculator'] == 'fd'):
			choice = 'fd'
			return redirect(url_for('fd'))
	else:
		print("Oooooopsy!")
	return render_template('index.html',choosen = choosen)


	
#Method for SIP Calculator Page

@app.route('/SIP',methods = ['GET','POST'])
def sip():
	
	sip_form = SIP_Form()
	if sip_form.validate_on_submit():
		session['monthly_investment'] = float(sip_form.monthly_investment.data)
		session['time_period'] = float(sip_form.time_period.data)
		session['expected_return_rate'] = float(sip_form.expected_return_rate.data)
		monthly_rate_of_return = session['expected_return_rate']/1200
		n = session['time_period'] * 12
		session['maturity_value']=round((session['monthly_investment'] * (1+monthly_rate_of_return) * ((pow((1+monthly_rate_of_return),n)) - 1)/monthly_rate_of_return),2)


		return redirect(url_for('result'))
	return render_template('SIP.html',sip_form = sip_form)



#Method For Lumpsum calculator page

@app.route('/lumpsum',methods = ['GET','POST'])
def lumpsum():
	lumpsum_form = LUMPSUM_Form()
	if lumpsum_form.validate_on_submit():
		session['lumpsum_investment'] = float(lumpsum_form.investment.data)
		session['lumpsum_rate'] = float(lumpsum_form.expected_return_rate.data)
		session['lumpsum_time_period'] = float(lumpsum_form.time_period.data)
		lumpsum_n = session['lumpsum_time_period']*12
		session['lumpsum_maturity_value'] = round(session['investment'] * ((1+ (session['lumpsum_rate']/100))**session['lumpsum_time_period']),2)
		return redirect(url_for('result'))
		
	return render_template('LUMPSUM.html',lumpsum_form = lumpsum_form)



@app.route('/fd',methods = ['GET','POST'])
def fd():
	fd_form = FD_Form()
	if fd_form.validate_on_submit():
		session['fd_investment'] = float(fd_form.investment.data)
		session['fd_rate_of_interest'] = float(fd_form.rate_of_interest.data)
		session['fd_time_period'] = float(fd_form.time_period.data)
		session['fd_maturity_value'] = (session['fd_investment']) + ((session['fd_investment'] * session['fd_rate_of_interest'] * session['fd_time_period'])/100)
		return redirect(url_for('result'))
		
	return render_template('FD.html',fd_form = fd_form)



#Method for result page

@app.route('/result',methods = ['GET','POST'])
def result():
	global choice
	print('Selected calculator is ' + choice)
	return render_template('result.html',choice = choice)


if __name__ == '__main__':
	app.run(debug=True)






