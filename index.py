from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,SubmitField,DecimalField)
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'izzasecret'


# SIP MATURITY VALUE FORMULA : FV = P [ (1+i)^n-1 ] * (1+i)/i
class SIP_Form(FlaskForm):
	name = StringField('Your name : ')
	monthly_investment = DecimalField('Your Monthly Investment')
	expected_return_rate = DecimalField('Return Rate : ')
	time_period = DecimalField('Time Period : ')
	virgin = BooleanField('Are you a virgin : ')
	submit = SubmitField('Submit')

@app.route('/',methods = ['GET','POST'])
def index():
	form = SIP_Form()
	if form.validate_on_submit():
		session['name'] = form.name.data
		session['virgin'] = form.virgin.data
		session['monthly_investment'] = form.monthly_investment.data
		session['time_period'] = form.time_period.data
		session['expected_return_rate'] = form.expected_return_rate.data
		# session['maturity_value'] = form.monthly_investment((1+form.expected_return_rate)**((form.time_period*12)-1)) * ((1+form.expected_return_rate)/form.expected_return_rate)
		return redirect(url_for('result'))

	return render_template('index.html',form = form)

@app.route('/result',methods = ['GET','POST'])
def result():
	return render_template('result.html')


if __name__ == '__main__':
	app.run(debug=True)






