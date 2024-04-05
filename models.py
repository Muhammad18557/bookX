"""This module contains the models for the application. It defines the database schema and the relationships between the tables."""

from flask_login import UserMixin
from database import db
from datetime import datetime


class User(db.Model, UserMixin):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return "<User %r %r>" % (self.name, self.id)


class Book(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("books", lazy=True))
    genre = db.Column(db.String(100), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    review = db.Column(db.Text, nullable=True)
    summary = db.Column(db.Text, nullable=True)
    likes = db.relationship("Like", backref="book", lazy="dynamic")

    def __repr__(self):
        return "<Book %r>" % self.title


class Like(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    timestamp = db.Column(db.DateTime, default=datetime.now)


class Exchange(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    book_id_a = db.Column(db.Integer, db.ForeignKey("book.id"))
    book_id_b = db.Column(db.Integer, db.ForeignKey("book.id"))
    user_id_a = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_id_b = db.Column(db.Integer, db.ForeignKey("user.id"))
    status = db.Column(db.String(20), default="pending")  # pening, accepted, rejected
    timestamp = db.Column(db.DateTime, default=datetime.now)


if __name__ == "__main__":
    from bookX import app

    with app.app_context():
        db.create_all()
