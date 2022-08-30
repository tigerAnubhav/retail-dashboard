from hmac import compare_digest

from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserSignUp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Name field can be empty")
    parser.add_argument("email", type=str, required=True, help="Email field can be empty")
    parser.add_argument("password", type=str, required=True, help="Password field can be empty")
    parser.add_argument(
        "company",
        type=str,
        required=False,
        default="Unemployed",
        help="Company field was left empty, it has been inserted as Unemployed",
    )

    def post(self):
        data = UserSignUp.parser.parse_args()
        user = UserModel.find_by_email(data["email"])

        if user:
            return {"message": f"A user with given email already exists having user id {user.id}", "status_code": 400}

        user = UserModel(**data)

        user.save_to_db()

        return {"message": f"User created successfully with user id {user.id}", "status_code": 200}


class UserSignIn(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Username required")
    parser.add_argument("password", type=str, required=True, help="Password Required")

    def post(self):
        data = UserSignIn.parser.parse_args()

        user = UserModel.find_by_email(data["email"])

        if user and compare_digest(user.password, data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)

            return (
                {
                    "token": access_token,
                    "user": {"id": user.id, "name": user.name, "email": user.email, "password": user.password},
                },
                200,
            )

        return {"message": "Invalid Credentials!"}, 401
