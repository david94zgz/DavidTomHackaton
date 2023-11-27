from flask import Flask
import pandas
import json
from datetime import datetime

app = Flask(__name__)


df = pandas.read_csv("data/vgsales.csv")
df['json'] = df.apply(lambda x:x.to_json(), axis=1)


@app.route("/")
def home():
    result = {
        "a_number_entries": str(df.size),
        "a_date_request": str(datetime.today()),
        "data": 
            [json.loads(x) for x in df['json'].to_dict().values()]
    }
    return result

@app.route("/<string:category>/<string:filter>")
def get_category(category, filter):
    df_selection = df.loc[df[category.capitalize()] == filter]
    result = {
        "a_number_entries": str(df_selection.size),
        "a_date_request": str(datetime.today()),
        "data": 
            [json.loads(x) for x in df_selection['json'].to_dict().values()]
    }
    return result