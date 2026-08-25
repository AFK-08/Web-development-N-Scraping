from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

class Login_Form(FlaskForm):
        email = StringField('Email')
        password = StringField('Password')


app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    form = Login_Form()
    return  render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      