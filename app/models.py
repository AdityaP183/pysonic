from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<User: {self.username} >"


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=False)

    songs = db.relationship("Song", backref="artist", lazy=True)

    def __repr__(self):
        return f"<Artist: {self.name} >"


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    release_date = db.Column(db.DateTime, nullable=True, default=datetime.now)
    song_thumbnail = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"))

    albumsong_id = db.relationship("AlbumSongs", backref="song", lazy=True)

    def __repr__(self):
        return f"<Song: {self.title} >"


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.DateTime, nullable=True, default=datetime.now)
    album_thumbnail = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=False)

    albumsong_id = db.relationship("AlbumSongs", backref="album", lazy=True)

    def __repr__(self):
        return f"<Song: {self.title} >"


class AlbumSongs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey("album.id"))
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"))
    created_by = db.Column(db.Integer, nullable=False)
