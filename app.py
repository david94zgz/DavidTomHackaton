from flask import Flask, render_template
import pandas
import json

app = Flask(__name__)


df = pandas.read_csv("data/vgsales.csv")

@app.route("/")
def home():
    result = {
    "num_entries": df.size,
        "data": 
            [json.loads(x) for x in df['json'].to_dict().values()]
    }
    return result

@app.route("genre/<string:genre>")
def get_genre(genre):
    df_selection = df.loc[df["Genre"] == genre]
    result = {
        "num_entries": df_selection.size,
        "data": 
            [json.loads(x) for x in df_selection['json'].to_dict().values()]
    }
    return result
