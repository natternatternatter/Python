from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "hellohellohello"


@app.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 0

    return render_template("index.html")


@app.route("/destroy_session")
def destroy_session():

    session.pop("counter")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
