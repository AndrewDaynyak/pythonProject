class Tv:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price    

    def switch_on(self):
        self.switched_on=True
        print(f'{self.brand} is switched on')

    def switch_off(self):
        self.switched_on=False
        print(f'{self.brand} is switched off')

class Fridge:
    def __init__(self, brand):
        self.brand=brand
        self.food=[]

    def whatsthere(self):
        print(f'In the fridge you have {self.food}')

    def add_food(self, food):
        self.food.append(food)
        print(f'Added {food} to the fridge')

    def remove_food(self, food):
        self.food.remove(food)
        print(f'Removed {food} from the fridge')

class Microwave:
    def __init__(self, brand):
        self.brand=brand
    def warm_up(self, food):
        print(F'{food} has just been warmed up!!!')

class Kitchen:
    def __init__(self, tv, fridge, microwave):
        self.tv=tv
        self.fridge=fridge
        self.microwave=microwave


tv1=Tv('Yandex', 40000)
fridge1=Fridge('Haier')
microwave1=Microwave('Gorenije')
kitchen1=Kitchen(tv1, fridge1, microwave1)

fridge1.add_food('Carrot')
fridge1.add_food('Shawarma')
fridge1.add_food('Apples')
print(kitchen1.fridge.whatsthere())


