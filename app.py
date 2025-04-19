from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# This block is mainly for local development.
# Render will use the start command (e.g., gunicorn) instead.
if __name__ == "__main__":
    # Use Render's PORT environment variable; default to 5000 for local dev
    port = int(os.environ.get("PORT", 5000))
    # Run the app, listening on all interfaces (0.0.0.0) as required by Render for the dev server
    # For production on Render, you'll use gunicorn which handles host/port via Render's settings.
    app.run(host="0.0.0.0", port=port)
