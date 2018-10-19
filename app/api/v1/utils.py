from flask import make_response, jsonify, abort
from validate_email import validate_email
import re

from .models import users


class Validator(object):
    '''User validations undertaken here'''
    def validate_credentials(self, data):
        self.email = data["email"]
        self.password = data["password"]
        self.role = data["role"]
        valid_email = validate_email(self.email)
        for user in users:
            if self.email == user["email"]:
                Message = "User already exists"
                abort(406, Message)
        if self.email == "" or self.password == "" or self.role == "":
            Message = "Kindly enter your full credentials"
            abort(400, Message)
        if not valid_email:
            Message = "Invalid email"
            abort(400, Message)
        elif len(self.password) < 6 or len(self.password) > 12:
            Message = "Password must be long than 6 characters or less than 12"
            abort(400, Message)
        elif not any(char.isdigit() for char in self.password):
            Message = "Password must have a digit"
            abort(400, Message)
        elif not any(char.isupper() for char in self.password):
            Message = "Password must have an upper case character"
            abort(400, Message)
        elif not any(char.islower() for char in self.password):
            Message = "Password must have a lower case character"
            abort(400, Message)
        elif not re.search("^.*(?=.*[@#$%^&+=]).*$", self.password):
            Message = "Password must have a special charater"
            abort(400, Message)


class Validator_products(object):
    def validate_product_description(self, data):
        '''Product descriptions validated here'''
        if len(data["description"]) < 20:
            Message = "Product description cant be less than 20 characters"
            abort(400, Message)
        if data["title"] == "" or data["category"] == "" or data["price"] == "" or data["quantity"] == "" or data["minimum_stock"] == "":
            Message = "All Product details ought to be filled up"
            abort(400, Message)