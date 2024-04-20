#!/usr/bin/python3
""" HBNB or Hello HBNB! Module """
from flask import Flask


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

if __name__ == "__main__":
    """ Changing port & host Flask listen to """
    app.run(debug=True, host='0.0.0.0', port=5000)
