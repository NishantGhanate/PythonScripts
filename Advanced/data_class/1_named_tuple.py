from typing import NamedTuple

class MyWorld(NamedTuple):
    name: str
    type: int = 0

my_world = MyWorld(name= 'Potato', type= 10)
print(my_world.name, my_world.type)

my_world = MyWorld(name= 'Oh no')
print(my_world.name, my_world.type)

print(my_world._fields)

new = my_world._replace(name='Oh yes')
print(new)


data = {'name': "Qt", 'type': 3.14}
word = MyWorld(**data)
print(word)