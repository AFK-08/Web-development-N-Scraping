from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("index.html",posts=all_posts)

@app.route("/post/<int:id>")
def get_post(id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, id=id)


if __name__ == "__main__":
    app.run(debug=True)
