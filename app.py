from flask import Flask
from flask_cors import CORS
from numpy import broadcast
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config["SECRET-KEY"] = "secret"
socketio = SocketIO(app, cors_allowed_origins=["http://127.0.0.1:5500"])


@socketio.on("message")
def handleMessage(msg):
    print("message: " + msg)
    send(msg, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug="true")
