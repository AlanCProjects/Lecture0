from flask import Flask, render_template, request
import forms


app = Flask(__name__)

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

