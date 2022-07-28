from hmac import compare_digest

from models.customer import CustomerModel


def authenticate(username, password):
    customer = CustomerModel.find_by_usename(username)
    if customer and compare_digest(customer.password, password):
        return customer


def identity(payload):
    customer_id = payload["identity"]
    return CustomerModel.find_by_id(customer_id)
