import os
from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from db import db

# from models.charts import ChartsMethod
from resources.charts import BoxPlot, CountPlot, PieChart, ScatterPlot
from resources.user import UserSignIn, UserSignUp

app = Flask(__name__)
app.secret_key = "Anubhav"
CORS(app)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=4380)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI", "sqlite:///data.db")

api.add_resource(UserSignIn, "/signin")
api.add_resource(UserSignUp, "/signup")
api.add_resource(PieChart, "/piechart")
api.add_resource(CountPlot, "/countplot")
api.add_resource(ScatterPlot, "/scatterplot")
api.add_resource(BoxPlot, "/boxplot")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
