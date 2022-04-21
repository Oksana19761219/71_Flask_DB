import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'books.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)



book_genres = db.Table('book_genres',
                        db.Column('book_id', db.Integer, db.ForeignKey('books.book_id')),
                        db.Column('genre_id', db.Integer, db.ForeignKey('genres.genre_id'))

)



book_authors = db.Table('book_authors',
                        db.Column('book_id', db.Integer, db.ForeignKey('books.book_id')),
                        db.Column('author_id', db.Integer, db.ForeignKey('authors.author_id'))

)


class Publisher(db.Model):
    __tablename__ = 'publishers'
    publisher_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    books = db.relationship('Book', backref='publisher')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    total_pages = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    isbn = db.Column(db.String(13))
    published_date = db.Column(db.String(10))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.publisher_id'))
    genres = db.relationship('Genre', secondary=book_genres, backref='books')
    authors = db.relationship('Author', secondary=book_authors, backref='books')

    def __init__(self, title, total_pages, rating, isbn, published_date):
        self.title = title
        self.total_pages = total_pages
        self.rating = rating
        self.isbn = isbn
        self.published_date = published_date

    def __repr__(self):
        return self.title


class Genre(db.Model):
    __tablename__ = 'genres'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(200))

    def __init__(self, genre):
        self.genre = genre

    def __repr__(self):
        return self.genre


class Author(db.Model):
    __tablename__ = 'authors'
    author_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    middle_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))

    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


db.create_all()