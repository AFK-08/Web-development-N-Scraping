from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

## CREATE DATABASE
class Base(DeclarativeBase):
    pass
## Configure the SQLite database, relative to the app instance folder:
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"

## Creating the Extension:
database = SQLAlchemy(model_class=Base)

## Initialize the app with the extension:
database.init_app(app)

## Creating the TABLE:
class Movies(database.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=True)

## Creating Table Schema in the database:
with app.app_context():
    database.create_all()


@app.route("/")
def home():
    ## Read All Records:
    with app.app_context():
        all_movies = database.session.query(Movies).all()
    return render_template("index.html",movies=all_movies)



if __name__ == '__main__':
    app.run(debug=True)
