from flask import Blueprint, request, jsonify, session

artist_bp = Blueprint("artist", __name__)

from app import db
from app.models import Artist


@artist_bp.route("/artist/create", methods=["POST"])
def artist_create():
    if request.is_json:
        artist_name = request.json.get("artistName")
        image = request.json.get("image")
        created_by = session.get("user_id")

        if created_by is None:
            return jsonify({"message": "User not logged in"}), 401

        new_artist = Artist(artist_name=artist_name, image=image, created_by=created_by)
        try:
            db.session.add(new_artist)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "Artist created successful"}), 201
    else:
        return "Request must contain JSON data", 400


@artist_bp.route("/artist/all", methods=["GET"])
def artist_getAll():
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    all_artist = Artist.query.all()
    return jsonify(
        [
            {
                "artistName": artist.artist_name,
                "image": artist.image,
                "createdBy": artist.created_by,
            }
            for artist in all_artist
        ]
    )


@artist_bp.route("/artist/<int:artist_id>", methods=["GET"])
def artist_getById(artist_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    artist = Artist.query.get(artist_id)

    if not artist:
        return (
            jsonify({"message": f"Artist not found with the given id = {artist_id}"}),
            404,
        )
    return (
        jsonify(
            {
                "artistName": artist.artist_name,
                "image": artist.image,
                "createdBy": artist.created_by,
            }
        ),
        200,
    )


@artist_bp.route("/artist/<artist_id>", methods=["PATCH"])
def artist_update(artist_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    if request.is_json:
        artist = Artist.query.get(artist_id)

        if not artist:
            return (
                jsonify(
                    {"message": f"Artist not found with the given id = {artist_id}"}
                ),
                404,
            )
        if artist and artist.created_by == session.get("user_id"):
            if "artistName" in request.json:
                artist.artist_name = request.json["artistName"]
            if "image" in request.json:
                artist.image = request.json["image"]

            try:
                db.session.commit()
            except Exception as e:
                return jsonify({"message": str(e)}), 400
            return jsonify({"message": "Artist updated successfully"}), 201
        else:
            return (
                jsonify({"message": "You are not allowed to update this artist"}),
                400,
            )
    else:
        return "Request must contain JSON data", 400


@artist_bp.route("/artist/<artist_id>", methods=["DELETE"])
def artist_delete(artist_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    artist = Artist.query.get(artist_id)

    if not artist:
        return (
            jsonify({"message": f"Artist not found with the given id = {artist_id}"}),
            404,
        )

    try:
        db.session.delete(artist)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message": "Artist deleted successfully"}), 201
