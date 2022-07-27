from flask import Flask
from random import randint


# lower and upper bounds for random number choices
LOWER = 1
UPPER = 20


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/rand_num")
def rand_element():
    return f"<h1>{randint(LOWER, UPPER)}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
