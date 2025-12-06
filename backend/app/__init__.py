from flask import Flask

def create_app():
    app = Flask(
        __name__,
        static_folder="../../frontend",
        template_folder="../../frontend"
    )

    # Register blueprint using relative import
    from .main import main
    app.register_blueprint(main)

    return app
