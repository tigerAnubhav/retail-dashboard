
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models.product import ProductModel


class ProductList(Resource):

    # @jwt_required()

    def get(self):
        prod1 = ProductModel(101, 'Umbrella')
        prod1.save_to_db()
        prod2 = ProductModel(102, ' Fossil Watch')
        prod2.save_to_db()
        prod3 = ProductModel(103, 'Footwear')
        prod3.save_to_db()
        prod4 = ProductModel(104, 'Blue shirt')
        prod4.save_to_db()
        prod5 = ProductModel(105, 'Ripped jeans')
        prod5.save_to_db()
        prod6 = ProductModel(106, 'Sweater')
        prod6.save_to_db()
        prod7 = ProductModel(107, 'Kids Wear')
        prod7.save_to_db()
        prod8 = ProductModel(108, 'Sun Glasses')
        prod8.save_to_db()
        prod9 = ProductModel(109, ' Casual Jwellery')
        prod9.save_to_db()
        prod10 = ProductModel(110, 'Tunics')
        prod10.save_to_db()

        return {"product_items": [x.json() for x in ProductModel.query.all()]}

