from flask import Flask,render_template,request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="POST":
        username = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        print(username,email,phone,message)
        return render_template("contact.html")
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)