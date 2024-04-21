#!/usr/bin/python3
""" Number template Module """
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    Method to display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    Method to display “HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun_or_cool(text):
    """
    Method to display “C + string”
    """
    text_replaced = text.replace("_", " ")
    return f"C {escape(text_replaced)}"


@app.route("/python/", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_more_fun(text):
    """
    Method to display “Python + string”
    """
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Method to display “n is a number”
    """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Method to display HTML page only if n is an integer
    """
    return render_template('5-number.html')


if __name__ == "__main__":
    """ Changing port & host Flask listen to """
    app.run(debug=True, host='0.0.0.0', port=5000)
