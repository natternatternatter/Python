from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def eight_by_eight():

    return render_template("index.html", y=4, x=4)


@app.route("/<int:x>")
def eight_by_four(x):
    x = x/2
    return render_template("index.html", x=x)


# @app.route("/<int:x>/<int:y>")
# def index(x, y):
#     return render_template("index.html", x=x, y=y)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
