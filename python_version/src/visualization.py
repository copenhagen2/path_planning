import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mlc
import matplotlib.animation as mla
import queue
import random

def show_map(map):
    color_map = mlc.ListedColormap(['white','red','blue','lightgreen','purple','black'])
    color_norm = mlc.Normalize(vmin=0,vmax=5)
    plt.pcolor(map,edgecolors='white',linewidths=1,cmap=color_map,norm=color_norm)
    plt.show()

def save_map(map, p):
    color_map = mlc.ListedColormap(['white','red','blue','lightgreen','purple','black'])
    color_norm = mlc.Normalize(vmin=0,vmax=5)
    plt.pcolor(map,edgecolors='white',linewidths=1,cmap=color_map,norm=color_norm)
    plt.savefig(p)