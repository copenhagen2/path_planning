import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mlc
import matplotlib.animation as mla
import time

def show_map(map):
    fig, ax = plt.subplots()
    color_map = mlc.ListedColormap(['white','red','blue','lightgreen','purple','black'])
    color_norm = mlc.Normalize(vmin=0,vmax=5)
    maze = plt.pcolormesh(map,edgecolors='white',linewidths=1,cmap=color_map,norm=color_norm)
    ax.set_aspect(1)
    plt.show()

def save_map(map, p):
    fig, ax = plt.subplots()
    color_map = mlc.ListedColormap(['white','red','blue','lightgreen','purple','black'])
    color_norm = mlc.Normalize(vmin=0,vmax=5)
    maze = plt.pcolormesh(map,edgecolors='white',linewidths=1,cmap=color_map,norm=color_norm)
    ax.set_aspect(1)
    plt.savefig(p)

def animation_show(map, search, path):
    fig, ax= plt.subplots()
    color_map = mlc.ListedColormap(['white','red','blue','lightgreen','purple','black'])
    color_norm = mlc.Normalize(vmin=0,vmax=5)
    n = len(search)
    m = len(path)
    maze = ax.pcolormesh(map,edgecolors='white',linewidths=1,cmap=color_map,norm=color_norm)
    ax.set_aspect(1)
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

def animation_save(map, search, path, f):
    fig, ax= plt.subplots()
    color_map = mlc.ListedColormap(['white','red','blue','lightgreen','purple','black'])
    color_norm = mlc.Normalize(vmin=0,vmax=5)
    n = len(search)
    m = len(path)
    maze = ax.pcolormesh(map,edgecolors='white',linewidths=1,cmap=color_map,norm=color_norm)
    ax.set_aspect(1)
    def update(frame):
        if frame >= n:
            x, y = path[frame-n]
            map[x][y] = 4
        else:
            x, y = search[frame]
            map[x][y] = 3
        maze.set_array(map)
        return maze,
    pw_writer = mla.PillowWriter(fps=50)
    ani = mla.FuncAnimation(fig, update, frames=n+m, interval=5, repeat=False)
    ani.save(f, writer=pw_writer)