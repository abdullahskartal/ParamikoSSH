from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class paraForm (FlaskForm):
	user = StringField("Username:")
	passwd = PasswordField ("Password:")
	destIp = StringField ("Destination IP:")
	command = StringField ("Command:")
	submit = SubmitField ("Send")
