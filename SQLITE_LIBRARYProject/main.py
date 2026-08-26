from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


## Creating Database:
class Base(DeclarativeBase):
    pass

## Configure the SQLite database, relative to the app instance folder:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

## Creating the Extension:
database = SQLAlchemy(model_class=Base)


## Initialize the app with the extension:
database.init_app(app)

## Creating TABLE:
class Books(database.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True,nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

## Creating Table Schema in the database:
with app.app_context():
    database.create_all()



## Home PAGE:
@app.route('/')
def home():

    ## Read All Records:
    with app.app_context():
        result = database.session.query(Books).all()
        all_books = result

    return render_template("index.html",books=all_books)

## ADD RECORD PAGE:
@app.route("/add",methods=["GET","POST"])
def add():

    if request.method=="POST":
        ## Creating a RECORD:
        with app.app_context():
            new_book = Books(title=request.form.get("name"),
                             author=request.form.get("author"),
                             rating=request.form.get("rating"))

            database.session.add(new_book)
            database.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True)

