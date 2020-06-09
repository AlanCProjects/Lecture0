from flask import Flask, render_template, request
import forms


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def Index():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data, comment_form.passwd.data)

    return render_template("index.html", form = comment_form)

if __name__ == '__main__':
    app.run(debug = True)

