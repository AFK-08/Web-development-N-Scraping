from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


## Create the app:
app = Flask(__name__)

## Creating Database:
class Base(DeclarativeBase):
    pass

## Configure the SQLite database, relative to the app instance folder:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books_collection.db"

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

## Creating a RECORD:
with app.app_context():
    new_book = Books(id=1,title="Harry Potter",author="JK Rowling",rating=9.5)

    database.session.add(new_book)
    database.session.commit()

