from flask import Blueprint, request, jsonify, session

song_bp = Blueprint("song", __name__)

from app import db
from app.models import Song


@song_bp.route("/song/create", methods=["POST"])
def song_create():
    if request.is_json:
        song_name = request.json.get("artistName")
        duration = request.json.get("duration")
        release_date = request.json.get("releaseDate")
        artist_id = request.json.get("artistId")
        song_thumbnail = request.json.get("songThumbnail")
        created_by = session.get("user_id")

        if created_by is None:
            return jsonify({"message": "User not logged in"}), 401

        new_song = Song(
            song_name=song_name,
            duration=duration,
            release_date=release_date,
            artist_id=artist_id,
            song_thumbnail=song_thumbnail,
            created_by=created_by,
        )
        try:
            db.session.add(new_song)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "Song created successfully"}), 201
    else:
        return "Request must contain JSON data", 400


@song_bp.route("/song/all", methods=["GET"])
def song_getAll():
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    all_song = Song.query.all()
    return jsonify(
        [
            {
                "songName": song.song_name,
                "duration": song.duration,
                "releaseDate": song.release_date,
                "artist": song.artist_id,
                "songThumbnail": song.song_thumbnail,
                "createdBy": song.created_by,
            }
            for song in all_song
        ]
    )


@song_bp.route("/song/<int:song_id>", methods=["GET"])
def song_getById(song_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    song = Song.query.get(song_id)

    if not song:
        return (
            jsonify({"message": f"Song not found with the given id = {song_id}"}),
            404,
        )
    return (
        jsonify(
            {
                "songName": song.song_name,
                "duration": song.duration,
                "releaseDate": song.release_date,
                "artist": song.artist_id,
                "songThumbnail": song.song_thumbnail,
                "createdBy": song.created_by,
            }
        ),
        200,
    )


@song_bp.route("/song/<song_id>", methods=["PATCH"])
def song_update(song_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    if request.is_json:
        song = Song.query.get(song_id)

        if not song:
            return (
                jsonify({"message": f"song not found with the given id = {song_id}"}),
                404,
            )
        if song and song.created_by == session.get("user_id"):
            if "songName" in request.json:
                song.song_name = request.json["songName"]
            if "duration" in request.json:
                song.duration = request.json["duration"]
            if "releaseDate" in request.json:
                song.release_date = request.json["releaseDate"]
            if "artist" in request.json:
                song.artist_id = request.json["artist"]
            if "songThumbnail" in request.json:
                song.song_thumbnail = request.json["songThumbnail"]

            try:
                db.session.commit()
            except Exception as e:
                return jsonify({"message": str(e)}), 400
            return jsonify({"message": "Song updated successfully"}), 201
        else:
            return (
                jsonify({"message": "You are not allowed to update this song"}),
                400,
            )
    else:
        return "Request must contain JSON data", 400


@song_bp.route("/song/<song_id>", methods=["DELETE"])
def artist_delete(song_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    song = Song.query.get(song_id)

    if not song:
        return (
            jsonify({"message": f"Artist not found with the given id = {song_id}"}),
            404,
        )

    try:
        db.session.delete(song)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message": "Song deleted successfully"}), 201
