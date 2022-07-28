from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.customer import CustomerRegister
from resources.product import ProductList
from resources.sales import (
    Average_sales_per_customer,
    PurchaseList,
    Sales,
    TotalSales,
    UniqueVisitors,
)
from security import authenticate, identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "anubhav"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(CustomerRegister, "/register")
api.add_resource(ProductList, "/products")
api.add_resource(Sales, "/sales")
api.add_resource(TotalSales, "/total_sales")
api.add_resource(UniqueVisitors, "/unique_visitors")
api.add_resource(Average_sales_per_customer, "/average_sale_per_customer")
api.add_resource(PurchaseList, "/daily_list")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
