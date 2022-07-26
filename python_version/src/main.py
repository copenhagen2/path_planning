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
    N = 40
    map = np.zeros((N, N))
    
    # Mark the border of the map
    for i in range(5,N-5):
        map[5][i] = 5
        map[N-6][i] = 5

    for i in range(5,N-5):
        map[i][5] = 5
        map[i][N-6] = 5

    # Mark the obstacles randomly
    for i in range(300):
        x = random.randint(6,N-6)
        y = random.randint(6,N-6)
        map[x][y] = 5
    
    # mark the start point and the end point
    s = (random.randint(6,N-7), random.randint(6,N-7))
    t = (random.randint(6,N-7), random.randint(6,N-7))
    map[s[0]][s[1]] = 1
    map[t[0]][t[1]] = 2  

    map_1 = np.array(map)
    map_2 = np.array(map)      
    map_3 = np.array(map)

    map_copy_1 = np.array(map)
    map_copy_2 = np.array(map)
    map_copy_3 = np.array(map)

    m, searched, path, cost = A_star.A_star(map_1, s, t, N)
    visualization.animation_save(map_copy_1,searched,path,r'G:\Summer Lab\path_planning\python_version\res\A_star.gif')
    print(f"A*: {cost}")

    m, searched, path, cost = bfs.bfs(map_2, s, t, N)
    visualization.animation_save(map_copy_2,searched,path,r'G:\Summer Lab\path_planning\python_version\res\bfs.gif')
    print(f"bfs: {cost}")

    m, searched, path, cost = dfs.dfs(map_3, s, t, N)
    visualization.animation_save(map_copy_3,searched,path,r'G:\Summer Lab\path_planning\python_version\res\dfs.gif')
    print(f"dfs: {cost}")