from backend.app import create_app

app = create_app()

# For Vercel to detect
if __name__ == "__main__":
    app.run()
