from flask import (
    Flask,
    render_template,
)
from random import randint


# lower and upper bounds for random number choices
LOWER = 1
UPPER = 20


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', who="World")


@app.route("/rand_num")
def rand_element():
    return f"<h1>{randint(LOWER, UPPER)}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
