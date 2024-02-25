from flask import Blueprint, request, jsonify, session

album_bp = Blueprint("album", __name__)

from app import db
from app.models import Album
