from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>"


@app.route("/bye")
def say_bye():
    return "<h1>Good</h1> <h2>Bye</h2>"

## Variables in Url:
@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"



## Some --name-- things:

if __name__ == "__main__":
    app.run(debug=True)


