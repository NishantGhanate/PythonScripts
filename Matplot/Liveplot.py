import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os 

scriptDir = os.path.dirname(os.path.realpath(__file__))

style.use('fivethirtyeight')

figure = plt.figure()
axis1 = figure.add_subplot(1,1,1)


def animate(i):
    graph_data = open(scriptDir + os.path.sep + 'example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x , y = line.split(',')
            xs.append(x)
            ys.append(y)
    
    axis1.clear()
    axis1.plot(xs,ys)



if __name__ =='__main__':
    ani = animation.FuncAnimation(figure,animate,interval=2000)
    plt.show()

