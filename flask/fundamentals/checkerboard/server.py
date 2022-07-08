from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def eight_by_eight(x=4, y=4):

    return render_template("index.html", y=y, x=x)


@app.route("/<int:x>")
def eight_by_four(x=4):
    return render_template("index.html", x=x, y=2)


@app.route("/<float:x>/<float:y>")
def index(x, y):
    return render_template("index.html", x=x, y=y)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
