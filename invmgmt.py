#we create an inventory management system, where the auditor inputs date and we print a table after every run.


class Product():

    def __init__(self,price, id, qoh):
        self.price = price
        self.id = id
        self.qoh = qoh


class Inventory(Product):

    def __init__(self, quantity):
        self.quantity = quantity

    def quantity():
        