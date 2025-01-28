from itertools import product

class food_store:
    def __init__(self, product):
        self.product=product
        self.products=[]

class Product:
    def __init__(self, product_name, delivery_data, shelf_life, price, expired=None):
        self.product_name=product_name
        self.delivery_data=delivery_data
        self.shelf_life=shelf_life
        self.price=price
        self.expired=False

    def create_product(self):
        product_name=input('Name of the product: ')
        delivery_data=input('Delivery data: ')
        shelf_life=input('Shelf life: ')
        price=input('Price: ')
        expired=input(bool('Expired?: '))
        product = Product(product_name, delivery_data, shelf_life, price,expired)
        return product

milk=Product('milk', '20.01.25', '14 days', 90, False)
cheese=Product('cheese', '18.01.25', '180 days', 350, False)
beer=Product('Zhigulevskoe', '15.01.25', '180 days', 100, False)
water=Product('Narzan', '29.01.25', '100 days', 50, False)



def product_info(self):
    return f"{self.product_name},{self.delivery_data},{self.shelf_life},{self.price},{self.expired}"


