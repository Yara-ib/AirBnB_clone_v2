#!/usr/bin/python3
""" HBNB or Hello HBNB! or C is fun!? Module """
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    Method to display “Hello HBNB!”

    Returns:
        string: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    Method to display “HBNB”

    Returns:
        string: HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun_or_cool(text):
    """
    Method to display “C + string”

    Returns:
        string: C + string
    """
    return f"C {text.replace("_", " ")}"


if __name__ == "__main__":
    """ Changing port & host Flask listen to """
    app.run(debug=True, host='0.0.0.0', port=5000)
