from datetime import date
from hmac import compare_digest

from models.customer import CustomerModel
from models.sales import SalesModel


def authenticate(username, password):
    # not able to provide validation by id
    user = CustomerModel.find_by_username(username)

    if user and compare_digest(user.password, password):
        visitor = SalesModel(user.id, 0, 0, date.today())
        visitor.save_to_db()
        return user


def identity(payload):
    user_id = payload["identity"]
    return CustomerModel.find_by_id(user_id)
