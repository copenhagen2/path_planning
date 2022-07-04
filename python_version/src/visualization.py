import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mlc
import matplotlib.animation as mla
import time

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

def animation_show(map, search, path):
    fig, ax= plt.subplots()
    color_map = mlc.ListedColormap(['white','red','blue','lightgreen','purple','black'])
    color_norm = mlc.Normalize(vmin=0,vmax=5)
    n = len(search)
    m = len(path)
    maze = ax.pcolormesh(map,edgecolors='white',linewidths=1,cmap=color_map,norm=color_norm)
    def update(frame):
        if frame >= n:
            x, y = path[frame-n]
            map[x][y] = 4
        else:
            x, y = search[frame]
            map[x][y] = 3
        maze.set_array(map)
        return maze,

    ani = mla.FuncAnimation(fig, update, frames=n+m, interval=5, repeat=False)
    plt.show()