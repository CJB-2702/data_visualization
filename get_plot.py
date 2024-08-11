from flask import Flask, render_template
import plotly.graph_objects as go
import plotly.io as pio
import json

app = Flask(__name__)

@app.route("/")
def index():
    x1 = [i for i in range(10)]
    y1 = x1.copy()

    x2 = x1.copy()
    y2 = [x*x for x in range(10)]

    #https://plotly.com/javascript/plotlyjs-function-reference/#plotlynewplot
    plot = {"data": None, "layout": None, "config":None}

    #https://plotly.com/javascript/reference/
    plot["data"] = [
        {"x": x1, "y": y1, "mode": "lines+markers"},
        {"x": x2, "y": y2, "mode": "lines+markers"}
    ]

    #https://plotly.com/javascript/reference/layout/
    plot["layout"] = {   
        "margin":{"autoexpand": False, "t":0}
    }

    #https://plotly.com/javascript/configuration-options/
    plot["config"]={}


    table_data = []#[{"x": x, "y": y} for x, y in zip(x1, y1)] #let user init

    return render_template("index.html", plot=plot, table_data=table_data)

if __name__ == "__main__":
    app.run(debug=True)