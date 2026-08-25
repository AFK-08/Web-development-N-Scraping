from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import Bootstrap5

## Making Login_Form Class with feilds for data entry:
class Login_Form(FlaskForm):
        email = StringField(label='Email',validators=[DataRequired(),Email(message="Enter valid Email")])

        password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8,message="Enter minimum 8 characters")])

        submit = SubmitField(label="LOGIN")

## Creating a Flask Server:
app = Flask(__name__)

## Using Flask_Bootsrap to load css:
bootstrap = Bootstrap5(app)

## WTF FORM CSFR key:
app.secret_key = 'mysecretkey'

@app.route("/")
def home():
    return render_template('index.html')

## Login Page:

@app.route("/login",methods=["GET","POST"]) 
def login():
    form = Login_Form()
    form.validate_on_submit()
    if form.validate_on_submit():
         if form.email.data=="admin@email.com" and form.password.data=="12345678":
              return render_template("success.html")
         else:
              return render_template("denied.html")
    return  render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      