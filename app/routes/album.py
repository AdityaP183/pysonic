from flask import Blueprint, request, jsonify, session

album_bp = Blueprint("album", __name__)

from app import db
from app.models import User
from app.models import Artist
from app.models import Song
from app.models import Album
from app.models import AlbumSongs

#! Main albums routes


@album_bp.route("/albums", methods=["POST"])
def album_create():
    if request.is_json:
        title = request.json.get("albumTitle")
        release_date = request.json.get("releaseDate")
        album_thumbnail = request.json.get("albumThumbnail")
        created_by = session.get("user_id")

        if created_by is None:
            return jsonify({"message": "User not logged in"}), 401

        new_album = Album(
            title=title,
            release_date=release_date,
            album_thumbnail=album_thumbnail,
            created_by=created_by,
        )
        try:
            db.session.add(new_album)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "Album created successfully"}), 201
    else:
        return "Request must contain JSON data", 400


@album_bp.route("/albums", methods=["GET"])
def albums_getAll():
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    all_albums = Album.query.all()
    all_sorted_albums = []

    for album in all_albums:

        user = User.query.get(album.created_by)
        all_songs = AlbumSongs.query.filter_by(album_id=album.id).all()
        songs = []

        for ids in all_songs:

            s = Song.query.get(ids.song_id)

            artist = Artist.query.get(s.artist_id)
            artist_user = User.query.get(artist.created_by)
            song_user = User.query.get(s.created_by)
            songs.append(
                {
                    "title": s.title,
                    "duration": s.duration,
                    "releaseDate": s.release_date,
                    "artist": {
                        "artistName": artist.name,
                        "image": artist.image,
                        "createdBy": artist_user.username,
                    },
                    "songThumbnail": s.song_thumbnail,
                    "createdBy": song_user.username,
                }
            )

        all_sorted_albums.append(
            {
                "albumId": album.id,
                "title": album.title,
                "releaseDate": album.release_date,
                "albumThumbnail": album.album_thumbnail,
                "createdBy": user.username,
                "songs": songs,
            }
        )

    return jsonify(all_sorted_albums), 200


@album_bp.route("/albums/<int:album_id>", methods=["GET"])
def album_getById(album_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    album = Album.query.get(album_id)

    if not album:
        return (
            jsonify({"message": f"Album not found with the given id = {album_id}"}),
            404,
        )

    user = User.query.get(album.created_by)
    all_songs = AlbumSongs.query.filter_by(album_id=album_id).all()

    songs = []

    for ids in all_songs:

        s = Song.query.get(ids.song_id)

        artist = Artist.query.get(s.artist_id)
        artist_user = User.query.get(artist.created_by)
        song_user = User.query.get(s.created_by)
        songs.append(
            {
                "title": s.title,
                "duration": s.duration,
                "releaseDate": s.release_date,
                "artist": {
                    "artistName": artist.name,
                    "image": artist.image,
                    "createdBy": artist_user.username,
                },
                "songThumbnail": s.song_thumbnail,
                "createdBy": song_user.username,
            }
        )

    single_album = {
        "albumId": album.id,
        "title": album.title,
        "releaseDate": album.release_date,
        "albumThumbnail": album.album_thumbnail,
        "createdBy": user.username,
        "songs": songs,
    }
    return (
        jsonify(single_album),
        200,
    )


@album_bp.route("/albums/<int:album_id>", methods=["PATCH"])
def album_update(album_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    if request.is_json:
        album = Album.query.get(album_id)

        if not album:
            return (
                jsonify({"message": f"song not found with the given id = {album_id}"}),
                404,
            )
        if album and album.created_by == session.get("user_id"):
            if "albumTitle" in request.json:
                album.title = request.json["albumTitle"]
            if "releaseDate" in request.json:
                album.release_date = request.json["releaseDate"]
            if "albumThumbnail" in request.json:
                album.album_thumbnail = request.json["albumThumbnail"]

            try:
                db.session.commit()
            except Exception as e:
                return jsonify({"message": str(e)}), 400
            return jsonify({"message": "Album updated successfully"}), 201
        else:
            return (
                jsonify({"message": "You are not allowed to update this album"}),
                400,
            )
    else:
        return "Request must contain JSON data", 400


@album_bp.route("/albums/<int:album_id>", methods=["DELETE"])
def album_delete(album_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    album = Album.query.get(album_id)

    if not album:
        return (
            jsonify({"message": f"Album not found with the given id = {album_id}"}),
            404,
        )

    try:
        db.session.delete(album)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message": "Song deleted successfully"}), 201


##! Albums insert and remove routes


@album_bp.route("/albums/<int:album_id>/add", methods=["POST"])
def album_song_add(album_id):
    if request.is_json:
        song_id = request.json.get("songId")
        created_by = session.get("user_id")

        if created_by is None:
            return jsonify({"message": "User not logged in"}), 401

        new_album_song = AlbumSongs(
            album_id=album_id, song_id=song_id, created_by=created_by
        )
        try:
            db.session.add(new_album_song)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "Added song to the album successfully"}), 201
    else:
        return "Request must contain JSON data", 400


@album_bp.route("/albums/<int:album_id>/remove", methods=["POST"])
def album_song_remove(album_id):
    if request.is_json:
        song_id = request.json.get("songId")
        created_by = session.get("user_id")

        if created_by is None:
            return jsonify({"message": "User not logged in"}), 401

        album_song = AlbumSongs.query.filter_by(
            album_id=album_id, song_id=song_id
        ).first()

        if album_song:
            try:
                db.session.delete(album_song)
                db.session.commit()
            except Exception as e:
                return jsonify({"message": str(e)}), 400
            return jsonify({"message": "Song deleted from album successfully"}), 200
        return jsonify({"message": "Not found the song in the album"}), 404
    else:
        return "Request must contain JSON data", 400
