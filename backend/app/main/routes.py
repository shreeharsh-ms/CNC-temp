from flask import send_from_directory
from . import main
import os

# Path to frontend folder
FRONTEND_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../frontend")
)

# ---------- MAIN ROUTES ----------
@main.route("/")
def home():
    return send_from_directory(FRONTEND_PATH, "home.html")

@main.route("/about")
def about():
    return send_from_directory(FRONTEND_PATH, "about-us.html")

@main.route("/contact")
def contact():
    return send_from_directory(FRONTEND_PATH, "contact_us.html")

@main.route("/menu")
def menu():
    return send_from_directory(FRONTEND_PATH, "menu.html")

@main.route("/chef")
def meet_chef():
    return send_from_directory(FRONTEND_PATH, "meet-chef.html")

@main.route("/coming-soon")
def coming_soon():
    return send_from_directory(FRONTEND_PATH, "Coming_soon.html")

@main.route("/Privacy-Policy")
def privacy_policy():
    return send_from_directory(FRONTEND_PATH, "privacy-policy.html")

@main.route("/terms-and-conditions")
def terms_and_conditions():
    return send_from_directory(FRONTEND_PATH, "Terms-and-conditions.html")

# ---------- STATIC FILES (CSS, JS, Images) ----------
@main.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(FRONTEND_PATH, filename)

# ---------- CUSTOM 404 PAGE ----------
@main.app_errorhandler(404)
def page_not_found(e):
    return send_from_directory(FRONTEND_PATH, "404.html"), 404

