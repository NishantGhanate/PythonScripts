from abc import ABC, abstractmethod  
  
class PenSubject(ABC):  
 
    @abstractmethod  
    def add(self, shop):  
        pass  
 
    @abstractmethod  
    def remove(self, shop):  
        pass  
 
    @abstractmethod  
    def notify(self):  
        pass 


class Pen(PenSubject):  
  
    def __init__(self, prize):  
        self._penPrize = prize
        self.shops = []    
  
  
    def add(self, shop):  
        self.shops.append(shop)  
  
    def remove(self, shop):  
        self.shops.remove(shop)
  
    def notify(self):  
        for shop in self.shops:  
            shop.update(self)  
        print('---------------------------------------')  
    
    # # https://www.programiz.com/python-programming/property
    @property  
    def penPrize(self):  
        return self._penPrize  
 
    @penPrize.setter  
    def penPrize(self, prize):  
        self._penPrize = prize  
        self.notify() 


class ShopObserver(ABC):  
 
    @abstractmethod  
    def update(self, pen):  
        pass  

class Shop(ShopObserver):  
  
    def __init__(self, shopName: str):  
        self._shopName = shopName  
  
    def update(self, pen: Pen):  
        print("pen prize changed to ", pen.penPrize, ' in ', self._shopName)  

if __name__ == '__main__':
    pen = Pen(10)  
    pen.add(Shop('Shop1'))  
    pen.add(Shop('Shop2'))  
    pen.add(Shop('Shop3'))  
    
    pen.penPrize = 15  
    pen.penPrize = 20  
    pen.penPrize = 32 