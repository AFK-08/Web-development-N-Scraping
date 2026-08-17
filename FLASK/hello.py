from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper
        


@app.route("/")
@make_bold
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Good Bye!"

## Variables in Url:
@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"



## Some --name-- things:

if __name__ == "__main__":
    app.run(debug=True)


