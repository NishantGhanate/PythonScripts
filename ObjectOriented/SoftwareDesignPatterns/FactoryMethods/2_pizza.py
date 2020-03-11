from abc import ABC, abstractmethod

#  Abstract Parent class 
class Pizza(ABC):

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        print("cutting pizza in pieces")

    def box(self):
        print("putting pizza in box")

# Child class will inherit parent class features , also it will override it
class NYStyleCheesePizza(Pizza):
    def prepare(self):
        print("preparing a New York style cheese pizza..")

    def bake(self):
        print('Baking NYStyleCheesePizza at 400 degrees for 12 mins')

class NYStyleGreekPizza(Pizza):
    def prepare(self):
        print("preparing a New York style greek pizza..")

    def bake(self):
        print('Baking NYStyleGreekPizza at 350 degrees for 10 mins')


# This time, PizzaStore is abstract
class PizzaStore(ABC):

  # We brought createPizza back into the PizzaStore (instead of the SimpleFactory)
  # However, it is declared as abstract. This time, instead of having
  # a factory class, we have a factory method:
  # function annotations 
  @abstractmethod
  def _createPizza(self, pizzaType: str) -> Pizza:
    pass

  def orderPizza(self, pizzaType):
    pizza: Pizza

    pizza = self._createPizza(pizzaType)

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()

class NYPizzaStore(PizzaStore):

  def _createPizza(self, pizzaType: str) -> Pizza:
    pizza: Pizza = None

    if pizzaType == 'Greek':
      pizza = NYStyleGreekPizza()
    elif pizzaType == 'Cheese':
      pizza = NYStyleCheesePizza()
    else:
      print("No matching pizza found in the NY pizza store...")
    
    return pizza

nyPizzaStore = NYPizzaStore()
print('\n')
nyPizzaStore.orderPizza('Greek')
print('\n')
nyPizzaStore.orderPizza('Cheese')