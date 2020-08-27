from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CsrfProtect
import forms


app = Flask(__name__)
app.secret_key = 'YC6B8E4IXc'
csr = CsrfProtect(app)

@app.route("/", methods = ['GET', 'POST'])
def Index():
    login_form = forms.LoginForm(request.form)
    regist_form = forms.RegistForm(request.form)

    if request.method == 'POST' and regist_form.validate():
        print(regist_form.username.data, regist_form.email.data, regist_form.passwd.data)

    elif request.method == 'POST' and login_form.validate():
        print('Logueado con', login_form.username.data, login_form.passwd.data)

    return render_template("index.html", forml = login_form, formr = regist_form)

if __name__ == '__main__':
    app.run(debug = True)

