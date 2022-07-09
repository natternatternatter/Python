from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "here we go"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_info", methods=["POST"])
def get_info():
    return redirect("/user_confirmation")


@app.route("/user_confirmation")
def user_confirmation():
    return render_template("user_confirmation.html")


if __name__ == "__main__":
    app.run(debug=True)
