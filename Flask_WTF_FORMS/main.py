from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class Login_Form(FlaskForm):
        email = StringField(label='Email',validators=[DataRequired(),Email(message="Enter valid Email")])

        password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8,message="Enter minimum 8 characters")])
        
        submit = SubmitField(label="LOGIN")

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route("/")
def home():
    return render_template('index.html')



@app.route("/login",methods=["GET","POST"]) 
def login():
    form = Login_Form()
    form.validate_on_submit()
    return  render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      