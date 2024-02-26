from flask import Blueprint, request, jsonify, session

album_bp = Blueprint("album", __name__)

from app import db
from app.models import Album


@album_bp.route("/albums", methods=["POST"])
def create_album():
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
def get_albums():
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    all_album = Album.query.all()
    return jsonify(
        [
            {
                "albumId": album.id,
                "title": album.title,
                "releaseDate": album.release_date,
                "albumThumbnail": album.album_thumbnail,
                "createdBy": album.created_by,
            }
            for album in all_album
        ]
    )


@album_bp.route("/albums/<int:album_id>", methods=["GET"])
def get_albumById(album_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    album = Album.query.get(album_id)

    if not album:
        return (
            jsonify({"message": f"Album not found with the given id = {album_id}"}),
            404,
        )
    return (
        jsonify(
            {
                "albumId": album.id,
                "title": album.title,
                "releaseDate": album.release_date,
                "albumThumbnail": album.album_thumbnail,
                "createdBy": album.created_by,
            }
        ),
        200,
    )


@album_bp.route("/albums/<int:album_id>", methods=["PATCH"])
def update_album(album_id):
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
