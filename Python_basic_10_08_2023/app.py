
"""
Main module contain the major fuctionalities of the application.
"""
from flask import Flask
from typing import Any
from functools import wraps
import os
import datetime
from dotenv import load_dotenv
import threading
from flask import Flask, render_template, request, jsonify
from jsonschema import validate
from flask_socketio import join_room, leave_room, send, SocketIO, emit
from random import random
from time import sleep
from threading import Thread, Event

# ngrok.set_auth_token("2T1O4uqRG1iUOaqPtGGsOIaTysW_5vcKQETZ7wVzDYebPxHn")
app = Flask(__name__)
# run_with_ngrok(app)

socketio = SocketIO(app)

@app.route("/")
def index():
    """
    default route.

    Parameters:
    ----------
    None

    Return:
    ------
    template
        render tempelate chat.html.
    """
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    """
    method will take the data and return the response in text form.

    Parameters:
    ----------
    None

    Return:
    ------
    str
        return the response in return of user text data.

    """
    message_data = request.form["msg"]
    data = "I am hard code message"+message_data
    return data

@socketio.on("text")
def handle_message(raw_text: str):
    """
    socket method to handle the nessage send by the user and return response.

    Parameters:
    ----------
    raw_text: str
        data or message send by the user to talk with chatbot.

    Return:
    ------
    response
        return response from the model in return of user message.

    """
    message = "I am hard code message"+raw_text
    send(message)

if __name__ == "__main__":
    socketio.run(app)
    #app.run()
