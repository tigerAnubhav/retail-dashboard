import sqlite3
from pathlib import Path

import pandas as pd
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Path("data.db").touch()

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

basketball_data = pd.read_csv("../database/CollegeBasketballPlayers2022_clean.csv")

basketball_data.to_sql("basketball", connection, if_exists="replace", index=False)

connection.commit()
connection.close()
