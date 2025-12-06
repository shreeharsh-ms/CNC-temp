from flask import Blueprint, send_from_directory
import os

main = Blueprint("main", __name__)

# Path to frontend folder
FRONTEND_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../frontend")
)

@main.route("/")
def home():
    return send_from_directory(FRONTEND_PATH, "home.html")

@main.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(FRONTEND_PATH, filename)
