from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.product import ProductModel


class ProductList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("product_id", type=int, required=True, help="This field cannot be left blank")
    parser.add_argument("product_des", type=str, required=True, help="This field cannot be left blank")

    def post(self):
        data = ProductList.parser.parse_args()

        if ProductModel.find_by_id(data["product_id"]):
            return {"message": "A product with that product_id already exists"}, 400

        product = ProductModel(**data)
        product.save_to_db()

        return {"message": "Product added successfully."}, 201

    @jwt_required()
    def get(self):
        return {"product_inventory": [x.json() for x in ProductModel.query.all()]}
