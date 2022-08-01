from flask_restful import Resource, reqparse
from models.customer import CustomerModel


class CustomerRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("fname", type=str, required=True, help="This field cannot be left blank")
    parser.add_argument("lname", type=str, required=True, help="This field cannot be left blank")
    parser.add_argument("username", type=str, required=True, help="This field cannot be left blank")
    parser.add_argument("password", type=str, required=True, help="This field cannot be left blank")

    def post(self):
        data = CustomerRegister.parser.parse_args()

        if CustomerModel.find_by_usename(data["username"]):
            return {"message": "A user with that username already exists"}, 400

        customer = CustomerModel(**data)
        customer.save_to_db()

        return {"message": "User created successfully."}, 201

    def get(self):
        return {"Customer Registered": [x.json() for x in CustomerModel.query.all()]}
