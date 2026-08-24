from flask import Flask, render_template,request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def recieve_data():
    username_data = request.form.get("username")
    password_data = request.form.get("password")
    return render_template("login.html",username=username_data,password=password_data)



if __name__=="__main__":
    app.run(debug=True)