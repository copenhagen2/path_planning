# build-in libs
import numpy as np
import random
import time

# private import
import bfs
import dfs
import A_star
import visualization

if __name__  == "__main__":
    map = np.zeros((50,50))
    
    # Mark the border of the map
    for i in range(5,45):
        map[5][i] = 5
        map[44][i] = 5

    for i in range(5,45):
        map[i][5] = 5
        map[i][44] = 5

    # Mark the obstacles randomly
    for i in range(300):
        x = random.randint(6,44)
        y = random.randint(6,44)
        map[x][y] = 5
    
    # mark the start point and the end point
    s = (random.randint(6,43), random.randint(6,43))
    t = (random.randint(6,43), random.randint(6,43))
    map[s[0]][s[1]] = 1
    map[t[0]][t[1]] = 2  

    map_1 = np.array(map)
    map_2 = np.array(map)      
    map_3 = np.array(map)

    map_1, searched, path = A_star.A_star(map_1, s, t)
    visualization.animation_show(map,searched,path)