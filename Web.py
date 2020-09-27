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
    error = '' #Use to catch errors to show the user
    user = ''
    #Forms
    login_form = forms.LoginForm(request.form)
    regist_form = forms.RegistForm(request.form)

    if 'username' in session:
        return redirect(url_for('Home'))

    if request.method == 'POST' and regist_form.validate():
        #Saber si el formulario enviado es el de registrarse, comprovando si los campos son validos
        try:
            sqlrequest.sqlinsert(regist_form.username.data, regist_form.email.data, regist_form.passwd.data)
            error = 'SUCCESS'

        except Exception as e:
                print(e)
                error = 'UNIQUE'

    elif request.method == 'POST' and login_form.validate():
        #Know if the user are interact with login form
        passwd = ''
        users = sqlrequest.sqlselect('user', 'name') #Load names of the users table of DB
        username = login_form.username.data #Save in username the username entered of the user
        
        if ( username in users):
            #Verify that the user exists
            passwd = sqlrequest.sqlselect('user', 'passwd', f'name ="{username}"')

            if (login_form.passwd.data in passwd):
                #Verify the password
                passwd.clear() #clear variable
                session['username'] = login_form.username.data
                return redirect(url_for('Home'))
            else:
                error = 'WRONG' 
        else:
            error = 'WRONG'

        users.clear() #clear variable
    
    if ('username' in session):
        user = session['username']

    return render_template("index.html", forml = login_form, formr = regist_form, user = user, error = error)

@app.route('/logout')
def Logout():
    #Close session
    if ('username' in session):
        session.pop('username')

    return redirect(url_for('Index'))

@app.route('/home')
def Home():
    if 'username'in session:
        user = session['username']
        return render_template('home.html', user = user)
    else: 
        return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
