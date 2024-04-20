#!/usr/bin/python3
""" Hello Flask! Module """
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


if __name__ == "__main__":
    """ Changing port & host Flask listen to """
    app.run(debug=True, host='0.0.0.0', port=5000)
