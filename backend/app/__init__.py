from flask import Flask
import os

def create_app():
    app = Flask(
        __name__,
        static_folder="../../frontend",
        template_folder="../../frontend"
    )

    # Register blueprints
    from app.main import main
    app.register_blueprint(main)

    return app
