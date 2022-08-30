from datetime import date
from hmac import compare_digest

from flask import make_response, render_template
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource, reqparse
from models.customer import CustomerModel
from models.sales import SalesModel
from security import authenticate, identity


class CustomerRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'firstname',
        type=str,
        required=True,
        help='This field cannot be lest blank'
        )
    parser.add_argument(
        'lastname',
        type=str,
        required=True,
        help='This field cannot be lest blank'
        )

    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be lest blank'
        )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be lest blank'
        )



    def post(self):

        data=CustomerRegister.parser.parse_args()

        user=CustomerModel.find_by_username(data['username'])

        if user:
            return {"mesaage":f"A user with given username already exists having user id {user.id}"} ,400

        user=CustomerModel(**data)

        user.save_to_db()

        return {"message":f"User created successfully with user id {user.id}"} ,201

    def get(self):
        return make_response(render_template('register.html'))

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Required: user name"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Required: password"
    )

    # def get(self):
    #     return make_response(render_template('login.html'))

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        user = CustomerModel.find_by_username(data['username'])

        if user and compare_digest(user.password, data['password']):

            access_token = create_access_token(identity=user.id, fresh=True)

            return {"token": access_token}, 200

        return {"message": "Invalid Credentials!"}, 401