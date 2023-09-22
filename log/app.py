# class About:
#     def __init__(self, name, view, year):
#         self.name = name
#         self.view = view
#         self.year = year
        
#     def BMW(self, x):
#         return f'{self.name},{x}, {self.view}'


# @About
# def about_car(self, x):
#     print('hello BMW', {x}, self.view, self.name)


# abo = About('BMWW', 'classic', 2012)
# about_car()


import types
from typing import Any


class App:
    x = {"eng": "hello"} 
    y = {"uz" : "salom"}
    # z = x + y

    def __call__(self, *args, **dicts):
        # x = f'{self.x}' 
        y = f'{self.y}' + f'{self.x}'
        return y
    

app = App()
print(app.__call__())