from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect, url_for
from flask_wtf.csrf import CSRFProtect
import forms

from static.db import sqlrequest


app = Flask(__name__)
app.secret_key = 'YC6B8E4IXc'
csr = CSRFProtect(app)

@app.route('/', methods = ['GET', 'POST'])
def Index():
    
    user = ''
    #Formularios
    login_form = forms.LoginForm(request.form)
    regist_form = forms.RegistForm(request.form)

    #
    if request.method == 'POST' and regist_form.validate():
        #Saber si el formulario enviado es el de registrarse, comprovando si los campos son validos
        try:
            sqlrequest.sqlinsert(regist_form.username.data, regist_form.email.data, regist_form.passwd.data)
        except Exception as e:
            print(e)

    elif request.method == 'POST' and login_form.validate():
        #Saber si se está interactuando con el formulario de login
        
        passwd = ''
        users = sqlrequest.sqlselect('user', 'name') #Carga los nombres de la tabla de usuarios de la BDD
        username = login_form.username.data
        
        if ( username in users):
            #Verifica que exista el usuario
            passwd = sqlrequest.sqlselect('user', 'passwd', f'name ="{username}"')

            if (login_form.passwd.data in passwd):
                #Comprueba la contraseña

                passwd.clear() #clear variable
                session['username'] = login_form.username.data
        users.clear() #clear variable
    
    if ('username' in session):
        user = session['username']
    return render_template("index.html", forml = login_form, formr = regist_form, user = user)

@app.route('/logout')
def Logout():
    if ('username' in session):
        session.pop('username')

    return redirect(url_for('Index'))

@app.route('/success')
def Success():
    return 'success'


if __name__ == '__main__':
    app.run(debug = True)
