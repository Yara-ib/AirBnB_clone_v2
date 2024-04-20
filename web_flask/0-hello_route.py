#!/usr/bin/python3
from flask import Flask
""" Hello Flask! Module """


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """
    Method to display “Hello HBNB!”

    Returns:
        string: Hello HBNB!
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
