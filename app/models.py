from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)


class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(255), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)


# class Song(db.Model):
#     song_id = db.Column(db.Integer, primary_key=True)
#     song_title = db.Column(db.String(255), nullable=False)
#     duration = db.Column(db.Integer, nullable=True)
#     release_date = db.Column(db.DateTime, nullable=True, default=datetime.now)
#     artist_id = db.Column(db.Integer, db.ForeignKey("artist.artist_id"), nullable=True)
#     song_thumbnail = db.Column(db.String(255), nullable=True)
#     created_by = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

#     artist = db.relationship("Artist", backref=db.backref("songs", lazy=True))


# class Album(db.Model):
#     album_id = db.Column(db.Integer, primary_key=True)
#     album_title = db.Column(db.String(255), nullable=False)
#     release_date = db.Column(db.DateTime, nullable=True, default=datetime.now)
#     artist_id = db.Column(db.Integer, db.ForeignKey("artist.artist_id"), nullable=True)
#     album_thumbnail = db.Column(db.String(255), nullable=True)
#     created_by = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

#     artist = db.relationship("Artist", backref=db.backref("albums", lazy=True))
#     album_songs = db.relationship("Song", backref=db.backref("album", lazy=True))
