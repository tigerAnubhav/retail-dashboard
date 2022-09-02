import sqlite3
from collections import Counter

import numpy as np
import pandas as pd
from flask_jwt_extended import jwt_required
from flask_restful import Resource


class PieChart(Resource):
    @jwt_required()
    def get(self):
        dataset = pd.read_sql_query("SELECT * FROM basketball", sqlite3.connect("data.db"))
        conference_count = dataset["conf"].to_list()
        x = list(Counter(conference_count).values())
        y = list(Counter(conference_count).keys())
        data = []
        for i in range(0, len(x)):
            data.append({"value": x[i], "name": y[i]})
        return {"x": data}


class CountPlot(Resource):
    @jwt_required()
    def get(self):
        dataset = pd.read_sql_query("SELECT * FROM basketball", sqlite3.connect("data.db"))
        role_column = dataset["role"].to_list()
        return {"x": list(Counter(role_column).keys()), "y": list(Counter(role_column).values())}


class ScatterPlot(Resource):
    @jwt_required()
    def get(self):
        dataset = pd.read_sql_query("SELECT * FROM basketball", sqlite3.connect("data.db"))
        data = np.array(dataset[["Min_per", "pts"]]).tolist()
        return {"x": data}


class BoxPlot(Resource):
    @jwt_required()
    def get(self):
        dataset = pd.read_sql_query("SELECT * FROM basketball", sqlite3.connect("data.db"))
        data = dataset.groupby("conf")["pts"].apply(list).reset_index(name="pts")
        return {"x": data["conf"].to_list(), "y": data["pts"].to_list()}
