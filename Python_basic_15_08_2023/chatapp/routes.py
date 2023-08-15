"""
Main route module.
"""
from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    """
    main route for teh application render teh main page of the application.

    Parameters:
    ----------
    None

    Return:
    ------
        render template chat.html.

    """
    return render_template("chat.html")
