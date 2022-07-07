from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/dojo")
def dojo():
    return "Dojo"


@app.route("/say/<string:name>")
def hi(name):
    return f"Hi " + name


@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    return f"{word} " * num


if __name__ == "__main__":
    app.run(debug=True, port=5001)
