"""
This file defines the routes for a flask application.
If run directly, it will spin up a development server.
"""

from random import randint

from flask import (
    Flask,
    render_template,
)


# lower and upper bounds for random number choices
LOWER = 1
UPPER = 20


app = Flask(__name__)


@app.route("/")
def index():
    """
    This route displays an HTML frontend Hello World

    :return: Rendered HTML template
    """
    return render_template('index.html', who="World")


@app.route("/rand_num")
def rand_num():
    """
    This route displays an HTML frontend random number

    :return: Rendered HTML template
    """
    return render_template("rand_num.html", num=randint(LOWER, UPPER))


if __name__ == "__main__":
    app.run(debug=True)
