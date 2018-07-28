import matplotlib.pyplot as plt
import numpy as np
from random import randint


# x and x1 , y and y1
plt.axis([0,10,0,10])


x=list()
y=list()

for i in range(10):
    temp_y= randint(0,10)
    x.append(i);
    y.append(temp_y);
    plt.scatter(i,temp_y);
    plt.pause(0.2) #Note this correction
    
    

plt.show()