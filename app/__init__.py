from flask import Flask
from config import Config
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# IMPORTANT: tell SocketIO to use eventlet, and allow your domain
socketio = SocketIO(
    app,
    async_mode="eventlet",
    cors_allowed_origins="*"   # or ["https://YOUR-APP.fly.dev"]
)
from app import routes, models
from app.models import Bible

@app.shell_context_processor
def make_shell_context():
    return { "db": db, "Bible": Bible }