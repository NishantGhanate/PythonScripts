from typing import List
from dataclasses import dataclass

@dataclass
class MyWorld:
    name: str
    type: int = 0

my_world = MyWorld(name= 'Potato', type= 10)
print(my_world.name, my_world.type)

my_world = MyWorld(name= 'Oh no')
print(my_world.name, my_world.type)

data = {'name': "Qt", 'type': 3.14}
word = MyWorld(**data)
print(word)


@dataclass
class Food:
    name : str

    def hows_it(self):
        print('{} is the best in the world'.format(self.name) )

wada_pav = Food(name= 'Mumbai wadapav')
wada_pav.hows_it()

@dataclass
class Menu:
    dishes : List[Food]


menu = Menu(dishes= [wada_pav, wada_pav])
print(menu)