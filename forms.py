from wtforms import Form, BooleanField, StringField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(Form):
    username = StringField('Username', validators=[
        DataRequired(message='Please fill this Field!'),
        Length(min=3, max=50, message='Username must be from 3 to 50 characters long.')
    ])
    password = PasswordField('PasswordField', validators=[
        DataRequired(message='Please fill this Field!')
    ])


class RegisterForm(Form):
    username = StringField('Username', validators=[
        DataRequired(message='Please fill this Field!'),
        Length(min=3, max=50, message='Username must be from 3 to 50 characters long.')
    ])
    phone = StringField('Phone number', validators=[
        DataRequired(message='Please fill this Field!'),
        Length(min=12, max=12, message='Phone number must be at least 12 characters long')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Please fill this Field!')
    ])
    confirm = PasswordField('Confirm Password', validators=[
        DataRequired(message='Please fill this Field!'),
        EqualTo(fieldname='password', message='Passwords must match!')
    ])
