from flask import Flask, render_template
import pandas

app = Flask(__name__)


cars = [{
    "licence_plate": "XBD9543D",
    "brand": "Toyota",
    "color": "Black",
    "price": 10
}]

df = pandas.read_csv("data/vgsales.csv")

@app.route("/")
def home():
    return df.to_json()
