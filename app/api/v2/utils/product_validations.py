from ..models.product_models import Product_Model
from flask import make_response, jsonify, abort


class Validator_products(object):
    def __init__(self, data):
        self.data = data

    def validate_data_types(self):
        '''Verifies data types of product details'''
        if len(self.data) > 6:
            Message = "Error, Excess fields given"
            abort(400, Message)
        try:
            self.data["price"] = float(self.data["price"])
            self.data["quantity"] = int(self.data["quantity"])
            self.data["minimum_stock"] = int(self.data["minimum_stock"])
        except:
            pass
        if type(self.data["title"]) is not str:
            Message = "Title field only accepts a string"
            abort(400, Message)

        if type(self.data["category"]) is not str:
            Message = "Category field only accepts a string"
            abort(400, Message)

        if type(self.data["price"]) is not float:
            Message = "Price field only accepts a float or an integer"
            abort(400, Message)

        if type(self.data["quantity"]) is not int:
            Message = "Quantity field only accepts an integer"
            abort(400, Message)

        if type(self.data["minimum_stock"]) is not int:
            Message = "Minimum stock field only accepts an integer"
            abort(400, Message)

        if len(self.data["description"]) < 20:
            Message = "Product description cant be less than 20 characters"
            abort(400, Message)

    def validate_missing_data(self):
        '''Checks for missing data keys in data
         passed during product registration'''

        if not self.data:
            Message = "No product details given yet"
            abort(400, Message)

        if "title" not in self.data:
            Message = "Product title key/field missing or mistyped"
            abort(400, Message)

        if "category" not in self.data:
            Message = "Product category key/field missing or mistyped"
            abort(400, Message)

        if "price" not in self.data:
            Message = "Product price key/field missing or mistyped"
            abort(400, Message)

        if "quantity" not in self.data:
            Message = "Product quantity key/field missing or mistyped"
            abort(400, Message)

        if "minimum_stock" not in self.data:
            Message = "Product minimum stock key/field missing or mistyped"
            abort(400, Message)

        if "description" not in self.data:
            Message = "Product description key/field missing or mistyped"
            abort(400, Message)

        if self.data["title"] == "":
            Message = "Product title is missing"
            abort(400, Message)

        if self.data["category"] == "":
            Message = "Product category is missing"
            abort(400, Message)

        if self.data["price"] == "":
            Message = "Product price is missing"
            abort(400, Message)

        if self.data["quantity"] == "":
            Message = "Product quantity is missing"
            abort(400, Message)

        if self.data["minimum_stock"] == "":
            Message = "Product minimum_stock is missing"
            abort(400, Message)

        if self.data["description"] == "":
            Message = "Product description is missing"
            abort(400, Message)

    def validate_duplication(self, data2):
        '''Checks if the product title to be
         registered already exists in database'''
        model = Product_Model()
        products = model.get()
        for product in products:
            if data2["title"] == product["title"]:
                Message = "Product already exists"
                abort(400, Message)

    def validate_negations(self):
        '''Checks to avoid any negative interger/float values 
        from being registered'''
        if self.data["price"] < 1 or self.data["quantity"] < 1 or self.data["minimum_stock"] < 0:
            Message = "Price, quantity or minmum stock cant be negative"
            abort(400, Message)

        if self.data["quantity"] < self.data["minimum_stock"]:
            Message = "Minmum stock cant be more than quantity"
            abort(400, Message)

    def strip_spaces(self):
        title = self.data["title"].strip().lower()
        category = self.data["category"].strip().lower()
        quantity = self.data["quantity"]
        price = self.data["price"]
        minimum_stock = self.data["minimum_stock"]
        description = self.data["description"].strip().lower()
        new_prod = {
            "title": title,
            "category": category,
            "quantity": quantity,
            "price": price,
            "minimum_stock": minimum_stock,
            "description": description
        }
        return new_prod
