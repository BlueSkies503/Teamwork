from flask import Flask
from random import randint


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/foo")
def rand_element():
    return f"<h1>{randint(1, 20)}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
