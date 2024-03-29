from flask import Blueprint, request, jsonify, session

artist_bp = Blueprint("artist", __name__)

from brain import db
from brain.models import Artist
from brain.models import User


@artist_bp.route("/artists", methods=["POST"])
def artist_create():
    if request.is_json:
        name = request.json.get("artistName")
        image = request.json.get("image")
        created_by = session.get("user_id")

        if created_by is None:
            return jsonify({"message": "User not logged in"}), 401

        if name is None:
            return jsonify({"message": "artistName is required"}), 400

        new_artist = Artist(name=name, image=image, created_by=created_by)
        try:
            db.session.add(new_artist)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "Artist created successful"}), 201
    else:
        return "Request must contain JSON data", 400


@artist_bp.route("/artists", methods=["GET"])
def artist_getAll():
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    all_artist = Artist.query.all()

    all_sorted_artist = []

    for artist in all_artist:
        user = User.query.get(artist.created_by)
        all_sorted_artist.append(
            {
                "artistName": artist.name,
                "image": artist.image,
                "createdBy": user.username,
            }
        )
    return jsonify(all_sorted_artist), 200


@artist_bp.route("/artists/<int:artist_id>", methods=["GET"])
def artist_getById(artist_id):
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401

    artist = Artist.query.get(artist_id)

    if not artist:
        return (
            jsonify({"message": f"Artist not found with the given id = {artist_id}"}),
            404,
        )

    user = User.query.get(artist.created_by)
    single_artist = {
        "artistName": artist.name,
        "image": artist.image,
        "createdBy": user.username,
    }
    return (
        jsonify(single_artist),
        200,
    )


@artist_bp.route("/artists/<artist_id>", methods=["PATCH"])
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
                artist.name = request.json["artistName"]
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


@artist_bp.route("/artists/<artist_id>", methods=["DELETE"])
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
