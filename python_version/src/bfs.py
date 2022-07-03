import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mlc
import matplotlib.animation as mla
import queue
import random

def bfs(map:np.array,s:tuple,t:tuple):
    que = queue.Queue() # the que to store the vertices
    que.put(s)
    pre = [[(-1,-1) for i in range(50)] for i in range(50)]
    visited = [[False for i in range(50)] for i in range(50)]
    visited[s[0]][s[1]] = True

    while not que.empty():
        v = que.get()
        v_x = v[0]
        v_y = v[1]
        if v != s:
            map[v_x][v_y] = 3 

        # suppose the robot can only move in four directions
        # right
        u = (v_x+1,v_y)
        u_x = u[0]
        u_y = u[1]
        if map[u_x][u_y] == 0 and not visited[u_x][u_y]:
            que.put(u)
            visited[u_x][u_y] = True
            pre[u_x][u_y] = v
        elif u == t:
            pre[u_x][u_y] = v
            break

        # left
        u = (v_x-1,v_y)
        u_x = u[0]
        u_y = u[1]
        if map[u_x][u_y] == 0 and not visited[u_x][u_y]:
            que.put(u)
            visited[u_x][u_y] = True
            pre[u_x][u_y] = v
        elif u == t:
            pre[u_x][u_y] = v
            break

        # up
        u = (v_x,v_y+1)
        u_x = u[0]
        u_y = u[1]
        if map[u_x][u_y] == 0 and not visited[u_x][u_y]:
            que.put(u)
            visited[u_x][u_y] = True
            pre[u_x][u_y] = v
        elif u == t:
            pre[u_x][u_y] = v
            break

        # down
        u = (v_x,v_y-1)
        u_x = u[0]
        u_y = u[1]
        if map[u_x][u_y] == 0 and not visited[u_x][u_y]:
            que.put(u)
            visited[u_x][u_y] = True
            pre[u_x][u_y] = v
        elif u == t:
            pre[u_x][u_y] = v
            break
    

    # recovery the path
    v = t
    while pre[v[0]][v[1]] != s:
        u = pre[v[0]][v[1]]
        map[u[0]][u[1]] = 4
        v = u
    
    return map




