from datetime import date

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.customer import CustomerModel
from models.sales import SalesModel


class Sales(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=int, required=True, help="This field cannot be blank.")
    parser.add_argument("product_id", type=int, required=True, help="This field cannot be blank.")
    parser.add_argument("sale_amount", type=int, required=True, help="This field cannot be blank.")
    parser.add_argument("sale_date", type=date, required=False, default=date.today(), help="This field can be blank.")

    # @jwt_required
    def post(self):
        data = Sales.parser.parse_args()

        if not CustomerModel.find_by_id(data["user_id"]):
            return {"message": "Please signup first"}

        sold_product = SalesModel(**data)

        sold_product.save_to_db()

        return {"message": "Sale Done successfully "}, 201


class PurchaseList(Resource):
    # @jwt_required()
    def get(self):
        return {
            "sold_items": [
                x.json() for x in SalesModel.find_by_date(date.today()).filter(SalesModel.sale_amount != 0).all()
            ]
        }


class UniqueVisitors(Resource):
    # @jwt_required()
    def get(self):
        visitors = SalesModel.find_by_date(date.today()).all()
        unique_visitor = len(set([visitor.user_id for visitor in visitors]))
        return {"unique_visitor": unique_visitor}


class TotalSales(Resource):
    # @jwt_required()
    def get(self):
        return {"total_sales": len(SalesModel.find_by_date(date.today()).filter(SalesModel.sale_amount != 0).all())}


class Average_sales_per_customer(Resource):
    # @jwt_required()
    def get(self):
        visitors = SalesModel.find_by_date(date.today()).all()
        unique_visitor = len(set([visitor.user_id for visitor in visitors]))
        total_sales = [visitor.sale_amount for visitor in visitors]
        var = sum(total_sales) / unique_visitor
        return {"var": var}
