#!/usr/bin/python3
from flask import Flask
""" Hello Flask! Module """


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Method to display “Hello HBNB!”

    Returns:
        string: Hello HBNB!
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    """ Changing port & host Flask listen to """
    app.run(host='0.0.0.0', port=5000)
