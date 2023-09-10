from flask import Blueprint, jsonify

homepage = Blueprint("homepage", __name__)


@homepage.route("/")
def home_page():
    return jsonify(message="welcome to homepage")
