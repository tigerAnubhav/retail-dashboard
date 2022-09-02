import csv
import sqlite3
from pathlib import Path

import pandas as pd
from db import db
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine


class ChartsMethod(db.Model):
    Path("data.db").touch()

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute(""" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='basketball' """)

    if cursor.fetchone()[0] == 0:
        basketball_data = pd.read_csv("../database/CollegeBasketballPlayers2022_clean.csv")
        basketball_data.to_sql("basketball", connection, index=False)
        connection.commit()

    connection.close()
