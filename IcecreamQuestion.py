class Item:
    def __init__(self,product_name,price,quantity):
        self.price = price
        self.product_name = product_name
        self.quantity = quantity

class Customer(Item):
    def __init__(self,product_name,price,quantity):
        Item.__init__(self,product_name,price, quantity)

class bill(Customer):
    def __init__(self,product_name,price,quantity):
        Customer.__init__(self,product_name,price,quantity)

    def print(self):
        print("Total Price :- ",self.price*self.quantity)

product_name = str(input())
price = int(input())
quantity = int(input())

cost = bill(product_name,price,quantity)
cost.print()