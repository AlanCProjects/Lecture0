from wtforms import Form, PasswordField, StringField, validators
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
    username = StringField('Nombre de usuario', [
        validators.Required(),
        validators.length(min=4, max=16, message='Caracteres minimos 4, maximos 16.')
        ])

    passwd = PasswordField('Contraseña',[
        validators.Required(),
        validators.length(min=6, max=20, message= 'La contraseña debe tener al menos 6 caracteres')
    ])

class RegistForm(Form):

    username = StringField('Nombre de usuario', [
        validators.Required(),
        validators.length(min=4, max=16, message='Caracteres minimos 4, maximos 16.')
        ])

    email = EmailField('E-mail', [validators.Required()])
    passwd = PasswordField('Contraseña',[
        validators.Required(),
        validators.length(min=6, max=20, message= 'La contraseña debe tener al menos 6 caracteres')
    ])
