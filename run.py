import os
from app import app, socketio

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    # Local dev: python run.py
    socketio.run(app, host="0.0.0.0", port=port, debug=False)