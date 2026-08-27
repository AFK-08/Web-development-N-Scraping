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



## Creating the Update Form:
class UpdateForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

## Read All Records and Display on Home Page:  
@app.route("/")
def home():
    ## Read All Records:
    with app.app_context():
        all_movies = database.session.query(Movies).all()
    return render_template("index.html",movies=all_movies)

    ## Sort the records based on rating and assign ranking:
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    database.session.commit()

## Edit Movie Record:
@app.route("/edit", methods=["GET","POST"])
def edit():
    ### Create Form Object:
    form = UpdateForm()
    movie_id = request.args.get("id")
    movie_to_update = database.session.query(Movies).get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        database.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",form=form,movie=movie_to_update)

## Delete Movie Record:
@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    delete_movie = database.session.query(Movies).get(movie_id)
    database.session.delete(delete_movie)
    database.session.commit()
    return redirect(url_for('home'))

## Creating the Add Movie Form:
class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

## ADD a New Movie Record:
@app.route("/add", methods=["GET","POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        ## Make an API Call to fetch the movie details:
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=API_KEY & query={movie_title}")
        data = response.json()
        results = data["results"]
        return render_template("select.html", options=results)
    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
