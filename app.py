from flask import Flask, render_template

app = Flask(__name__)


cars = [{
    "licence_plate": "XBD9543D",
    "brand": "Toyota",
    "color": "Black",
    "price": 10
}]


@app.route("/")
def home():
    return render_template("index.html")