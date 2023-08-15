"""
routes module contain the routes for different functionalities.
"""
from flask_socketio import emit, send
from .extensions import socketio
from modules import module_chat

@socketio.on("connect")
def handle_connect():
    """
    method print the message on console when a client is connected.

    Parameters:
    ----------
    None

    Return:
    ------
    None.

    """
    print("Client connected!")

@socketio.on("new_message")
def handle_new_message(message: str, methods = ['GET', 'POST'])-> str:
    """
    method will take a message from socket.emit method.

    Parameters:
    ----------
    None

    Return:
    ------
    message_response: str
        return the message return by the model.
    """
    my_message = "Hard code message"
    socketio.emit("chat", module_chat.get_Chat_response(message))
