from itertools import product

class Product:
    def __init__(self, product_name, production_date, shelf_life, price, expired=None):
        self.product_name=product_name
        self.production_date=production_date
        self.shelf_life=shelf_life
        self.price=price
        self.expired=False



class Factory:
    def make_product(self):
        product_name = input('Enter the name for the product:')
        production_date = input('Enter the production date for the product:')
        shelf_life = input('Enter the shelf-life for the product:')
        price = input('Enter the price of the product:')
        expired = input('Expired?:')
        nameoftheproduct = Product(product_name, production_date, shelf_life, price, expired)
        return product


milk=Product('milk', '20.01.25', '14 days', 90, False)
cheese=Product('cheese', '18.01.25', '180 days', 350, False)
beer=Product('Zhigulevskoe', '15.01.25', '180 days', 100, False)
water=Product('Narzan', '29.01.25', '100 days', 50, False)



def product_info(self):
    return f"{self.product_name},{self.production_date},{self.shelf_life},{self.price},{self.expired}"



