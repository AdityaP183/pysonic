from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)
from brain import db
from brain.models import User


@auth_bp.route("/auth/register", methods=["POST"])
def user_register():
    if request.is_json:
        username = request.json.get("username")
        email = request.json.get("email")
        password = str(request.json.get("password"))

        new_user = User(
            username=username, email=email, password=generate_password_hash(password)
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "User registration successfully"}), 201
    else:
        return "Request must contain JSON data", 400


@auth_bp.route("/auth/login", methods=["POST"])
def user_login():
    if request.is_json:
        email = request.json.get("email")
        password = str(request.json.get("password"))

        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify({"message": "No user registered with the given email"}), 404
        else:
            if user and check_password_hash(user.password, password):
                session["user_id"] = user.id
                return jsonify({"message": "User login successfully"}), 200
            return jsonify({"message": "User login failed", "data": user}), 401
    else:
        return "Request must contain JSON data", 400


@auth_bp.route("/auth/logout", methods=["GET"])
def user_logout():
    session.pop("user_id", None)
    return jsonify({"message": "User logged out successfully"}), 200


@auth_bp.route("/auth/current-user", methods=["GET"])
def current_user():
    if session.get("user_id") is None:
        return jsonify({"message": "User not logged in"}), 401
    user = User.query.get(session.get("user_id"))
    if not user:
        return (
            jsonify({"message": f"User not found"}),
            404,
        )
    return jsonify({"username": user.username, "email": user.email}), 200
