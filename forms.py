from wtforms import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms import validators
from wtforms import TextField
from wtforms import HiddenField
from wtforms.fields.html5 import EmailField

def Leng_Honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio.')

class LoginForm(Form):
    username = StringField('Nombre de usuario', [
        validators.Required(),
        validators.length(min=4, max=16, message='Caracteres minimos 4, maximos 16.')
        ])

    passwd = PasswordField('Contraseña',[
        validators.Required(),
        validators.length(min=6, max=20, message= 'La contraseña debe tener al menos 6 caracteres')
    ])

    honeypot = HiddenField('', [Leng_Honeypot])

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

    honeypot = HiddenField('', [Leng_Honeypot])
