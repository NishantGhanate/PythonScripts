# Spagetti code self reference , Read from line 53/60 main and easy to understand 

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import argparse , os , sys , re , time


# fivethirtyeight , seaborn , ggplot , dark_background , seaborn-dark
plt.style.use('ggplot')
# plt.rcParams.update({'font.size': 10})
# matplotlib.rcParams.update({'font.size': 10})

class Animation:
    def __init__(self):
       pass 

    def display(self):
        fig, ax = plt.subplots(figsize=(12,8))
        ax.axis(BBox)
        ax.set_title('Title : {}'.format(title))
        linestyle = ['-rp', '-bp' ,'-gp' , '-cp', '-mp' ,'-kp', '-gp','-yp'  , '-rd' , '-bd' , '-gd' , '-cd' , '-md'] 
        textX = 0.86
        textY = 0.96
        for i in range(count):
            lines[i], = ax.plot(data[i],bata[i], linestyle[i] ,alpha= 0.5 , ms=5 , label=names[i] , linewidth = 2.5 )
            time_texts[i] = ax.text(textX ,textY , '', fontsize=9,  transform=ax.transAxes)
            ax.legend(loc="upper right" , bbox_to_anchor=(1.12, 1))
            textY -= 0.04

        def animate(i):
            for c in range(count):
                lines[c].set_data(data[c] , bata[c])
                try :
                    time_texts[c].set_text(data[c]['date'] )
                except:
                    time_texts[c].set_text('')
            return lines,time_texts
        
        plot_backend = matplotlib.get_backend()
        mng = plt.get_current_fig_manager()
        if plot_backend == 'TkAgg':
            mng.resize(*mng.window.maxsize())
        elif plot_backend == 'wxAgg':
            mng.frame.Maximize(True)
        elif plot_backend == 'Qt4Agg':
            mng.window.showMaximized()

        if outputFile :
            try :
                simulation = animation.FuncAnimation(fig, animate, blit=False, frames=420, interval=69, repeat=False)
                savePath = 'output.mp4'
                simulation.save(filename=savePath,fps=4,dpi=100)
                plt.show()
            except Exception as e :
                print('\n[ Error ] : Possibly due to ffmpeg not in system path . Please view Readme.md file Downloads section '.format(e))
        else:
            simulation = animation.FuncAnimation(fig, animate, blit=False, frames=420, interval=69, repeat=True)
            plt.show()
        
if __name__ == '__main__':
      pass
    
