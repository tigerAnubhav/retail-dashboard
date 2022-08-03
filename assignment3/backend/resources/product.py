from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models.product import ProductModel


class ProductList(Resource):

    # @jwt_required()

    def get(self):
        prod1 = ProductModel(101, "Basketball Backboards")
        prod1.save_to_db()
        prod2 = ProductModel(102, "Basketball Pole")
        prod2.save_to_db()
        prod3 = ProductModel(103, "Basketball")
        prod3.save_to_db()
        prod4 = ProductModel(104, "Basketball Ring")
        prod4.save_to_db()
        prod5 = ProductModel(105, "Basketball Nets")
        prod5.save_to_db()
        prod6 = ProductModel(106, "Basketball Hoop")
        prod6.save_to_db()
        prod7 = ProductModel(107, "Basketball Set")
        prod7.save_to_db()
        prod8 = ProductModel(108, "Basketball Socks")
        prod8.save_to_db()
        prod9 = ProductModel(109, "Basketball Jersey")
        prod9.save_to_db()
        prod10 = ProductModel(110, "Basketball Court")
        prod10.save_to_db()

        return {"product_items": [x.json() for x in ProductModel.query.all()]}

