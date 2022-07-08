from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    print(request.form["strawberry"])
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    total = int(request.form["strawberry"]) + \
        int(request.form["raspberry"]) + int(request.form["apple"])
    print(f"Charging {first_name} {last_name} for {total} fruits.")
    return render_template("checkout.html", total=total)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
