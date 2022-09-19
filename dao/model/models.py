from sqlalchemy import Integer, String, Float
from setup_db import db


class Director(db.Model):
    __tablename__ = "director"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)


class Genre(db.Model):
    __table_name__ = 'genre'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)


class Movie(db.Model):
    __table_name__ = 'movie'
    id = db.Column(Integer, primary_key=True)
    description = db.Column(String)
    rating = db.Column(Float)
    title = db.Column(String)
    trailer = db.Column(String)
    year = db.Column(Integer)
    director_id = db.Column(Integer, db.ForeignKey(f"{Director.__tablename__}.id"))
    genre_id = db.Column(Integer, db.ForeignKey(f"{Genre.__tablename__}.id"))
    director = db.relationship("Director")
    genre = db.relationship("Genre")
