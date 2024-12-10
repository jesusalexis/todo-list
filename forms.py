from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, DateField
from wtforms.validators import DataRequired, Email, Length, Optional


class UserForm(FlaskForm):

    username = StringField(
        'Nickname:', 
        validators=[DataRequired(), Length(min=3, max=20, message="El nombre de usuario debe tener entre 3 y 20 caracteres.")]
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired(), Length(min=6, message="La contraseña debe tener al menos 6 caracteres.")]
    )
    email = StringField(
        'Email', 
        validators=[DataRequired(),Length(max=254),  Email(message="Debe ingresar un correo electrónico válido.")]
    )
    name = StringField(
        'Name', 
        validators=[Length(max=80, message="El nombre no debe exceder los 80 caracteres.")]
    )
    lastname = StringField(
        'Lastname', 
        validators=[Length(max=80, message="El apellido no debe exceder los 80 caracteres.")]
    )
    address = StringField(
        'Address', 
        validators=[Length(max=80, message="La dirección no debe exceder los 80 caracteres.")]
    )
    gender = SelectField(
        'Gender', 
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], 
        validators=[Optional()]
    )
    language = SelectField(
        'Language', 
        choices=[('ingles', 'Ingles'), ('español', 'Español'), ('frances', 'frances')], 
        validators=[Optional()]
    )
    birthday = DateField(
        'Birthday', 
        format='%Y-%m-%d', 
        validators=[Optional()]
    )
    submit = SubmitField('Registrar')

