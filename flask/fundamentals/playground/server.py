from flask import Flask, render_template
app = Flask(__name__)


@app.route("/play")
def blue_three():
    return render_template("index.html", num=3)


@app.route("/play/<int:num>")
def blue_number(num):
    return render_template("index.html", num=num)


@app.route("/play/<int:num>/<string:color>")
def color_number(color, num):
    return render_template("index.html", color=color, num=num)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
