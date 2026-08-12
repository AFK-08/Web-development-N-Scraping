from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "Good Bye"

## Variables in Url:
@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"



## Some --name-- things:

if __name__ == "__main__":
    app.run(debug=True)


