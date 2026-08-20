from flask import Flask,render_template
import requests

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello >> use /guess/name in the url"

@app.route("/guess/<name>")
def guess(name):
    
    ## Using APIs to get age and gender 

    parameters = {
        "name":name}
    
    agify_response = requests.get("https://api.agify.io", params=parameters)
    genderize_response = requests.get("https://api.genderize.io", params=parameters)
    gender = genderize_response.json()["gender"]
    age = agify_response.json()["age"]

    ## rendering html page:

    return render_template("index.html",username=name,user_age=age,gender=gender)


if __name__ == "__main__":
    app.run(debug=True)