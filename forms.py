from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

    username = StringField('Nickname', validators=[DataRequired(), Length(max=20)])
    password = StringField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Nombre', validators=[DataRequired(), Length(max=20)])
    lastname = StringField('Apellido', validators=[DataRequired(), Length(max=20)])
    address = StringField('Direccion', validators=[DataRequired(), Length(max=20)])
    gender = StringField('Genero', validators=[DataRequired(), Length(max=20)]) 
    language = StringField('Idioma', validators=[DataRequired(), Length(max=20)])
    birthday = StringField('Cumple', validators=[DataRequired(), Length(max=20)])

    username = StringField(
        'Username', 
        validators=[DataRequired(), Length(min=3, max=20, message="El nombre de usuario debe tener entre 3 y 20 caracteres.")]
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired(), Length(min=6, message="La contraseña debe tener al menos 6 caracteres.")]
    )
    email = StringField(
        'Email', 
        validators=[DataRequired(), Email(message="Debe ingresar un correo electrónico válido.")]
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
    language = StringField(
        'Language', 
        validators=[Length(max=50, message="El idioma no debe exceder los 50 caracteres.")]
    )
    birthday = DateField(
        'Birthday', 
        format='%Y-%m-%d', 
        validators=[Optional()]
    )
    submit = SubmitField('Submit')

