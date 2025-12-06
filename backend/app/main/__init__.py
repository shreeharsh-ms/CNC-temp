from flask import Blueprint

# Define the Blueprint
main = Blueprint("main", __name__)

# Import routes so they are registered with the blueprint
from . import routes
