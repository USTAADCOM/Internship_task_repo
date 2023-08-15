"""
Main application module which will execute the appllication.
"""
from chatapp import create_app, socketio
app = create_app()
socketio.run(app, debug = True)
