from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please enter another username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please enter another email.')


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField()
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField(validators=[DataRequired(), Email()])
    picture = FileField('Upload', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exists. Please enter another username.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Username already exists. Please enter another username.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. Please register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField(validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject')
    content = TextAreaField('Message')
    submit = SubmitField('Send')
