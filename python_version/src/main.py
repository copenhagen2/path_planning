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
    N = 50
    map = np.zeros((N, N))
    
    # Mark the border of the map
    for i in range(5,N-5):
        map[5][i] = 5
        map[N-6][i] = 5

    for i in range(5,N-5):
        map[i][5] = 5
        map[i][N-6] = 5

    # Mark the obstacles randomly
    for i in range(5,27):
        map[i][17] = 5
    for i in range(43,18,-1):
        map[i][35] = 5
    for i in range(30,40):
        map[19][i] = 5

    # mark the start point and the end point
    s = (10,10)
    t = (40,40)
    map[s[0]][s[1]] = 1
    map[t[0]][t[1]] = 2  

    map_1 = np.array(map)
    map_2 = np.array(map)      
    map_3 = np.array(map)

    map_copy_1 = np.array(map)
    map_copy_2 = np.array(map)
    map_copy_3 = np.array(map)

    m, searched, path, cost = A_star.A_star(map_1, s, t, N)
    print(f"A*: {cost}")
    visualization.animation_save(map_copy_1,searched,path,r'G:\Summer Lab\path_planning\python_version\res\A_star.gif')
    
    m, searched, path, cost = bfs.bfs(map_2, s, t, N)
    print(f"bfs: {cost}")
    visualization.animation_save(map_copy_2,searched,path,r'G:\Summer Lab\path_planning\python_version\res\bfs.gif')
    
    m, searched, path, cost = dfs.dfs(map_3, s, t, N)
    print(f"dfs: {cost}")
    visualization.animation_save(map_copy_3,searched,path,r'G:\Summer Lab\path_planning\python_version\res\dfs.gif')
    