from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .User import *
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.fetch_username(username.data)
		if user:
			raise ValidationError("This username is already taken. Please use a different one")

	def validate_email(self, email):
		user = User.fetch(email.data)
		if user:
			raise ValidationError("This email is already taken. Please use a different one")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ProfileForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=15)])
	status = StringField('Status', validators=[DataRequired()])
	age = IntegerField('Age', validators=[DataRequired()])
	lives = StringField('Lives in', validators=[DataRequired()])
	place = StringField('Hometown', validators=[DataRequired()])
	image = FileField('Upload a new Profile Picture', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update Profile')

	def check_username(self, username):
		user = User.fetch_username(username.data)
		if user:
			raise ValidationError("This username is already taken. Please use a different one")

	def check_email(self, email):
		user = User.fetch(email.data)
		if user:
			raise ValidationError("This email is already taken. Please use a different one")		

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	picture = FileField('Upload a picture?', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Post')

