from socket import socket
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

messages = []

app = Flask(__name__)
io = SocketIO(app)

@app.route('/')
def home():
        return render_template('chat.html')

@io.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg)
    emit('getMessage',msg , broadcast=True)

if __name__ == "__main__":
    io.run(app,debug=True)