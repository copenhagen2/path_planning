import numpy as np
import queue
import time

def Manhanttan_distance(u:tuple, v:tuple):
    x = np.abs(u[0]-v[0])
    y = np.abs(u[1]-v[1])
    return x + y

def A_star(map:np.array, s:tuple, t:tuple, N):
    q = queue.PriorityQueue()
    q.put((Manhanttan_distance(s,t),s))
    g = [[np.inf for i in range(N)] for i in range(N)]
    g[s[0]][s[1]] = 0
    f = [[np.inf for i in range(N)] for i in range(N)]
    f[s[0]][s[1]] = Manhanttan_distance(s,t)
    pre = [[(-1,-1) for i in range(N)] for i in range(N)]
    visited = [[False for i in range(N)] for i in range(N)]

    # return value
    searched = []
    path = []

    t_start = time.time()

    while not q.empty():
        cost, v = q.get()
        x_v = v[0]
        y_v = v[1]
        if visited[x_v][y_v]:
            continue
        visited[x_v][y_v] = True
        if v != s:
            map[x_v][y_v] = 3
            searched.append(v)

        # up
        u = (x_v, y_v+1)
        x_u = u[0]
        y_u = u[1]
        if u == t:
            pre[x_u][y_u] = v
            break
        tmp = g[x_v][y_v] + 1
        if map[x_u][y_u] == 0:
            if tmp < g[x_u][y_u]:
                g[x_u][y_u] = tmp
                f[x_u][y_u] = tmp + Manhanttan_distance(u,t)
                pre[x_u][y_u] = v
                q.put((f[x_u][y_u],u))

        # down
        u = (x_v, y_v-1)
        x_u = u[0]
        y_u = u[1]
        if u == t:
            pre[x_u][y_u] = v
            break
        tmp = g[x_v][y_v] + 1
        if map[x_u][y_u] == 0:
            if tmp < g[x_u][y_u]:
                g[x_u][y_u] = tmp
                f[x_u][y_u] = tmp + Manhanttan_distance(u,t)
                pre[x_u][y_u] = v
                q.put((f[x_u][y_u],u))
                

        # right
        u = (x_v+1, y_v)
        x_u = u[0]
        y_u = u[1]
        if u == t:
            pre[x_u][y_u] = v
            break
        tmp = g[x_v][y_v] + 1
        if map[x_u][y_u] == 0:
            if tmp < g[x_u][y_u]:
                g[x_u][y_u] = tmp
                f[x_u][y_u] = tmp + Manhanttan_distance(u,t)
                pre[x_u][y_u] = v
                q.put((f[x_u][y_u],u))
                

        # left
        u = (x_v-1, y_v)
        x_u = u[0]
        y_u = u[1]
        if u == t:
            pre[x_u][y_u] = v
            break
        tmp = g[x_v][y_v] + 1
        if map[x_u][y_u] == 0:
            if tmp < g[x_u][y_u]:
                g[x_u][y_u] = tmp
                f[x_u][y_u] = tmp + Manhanttan_distance(u,t)
                pre[x_u][y_u] = v
                q.put((f[x_u][y_u],u))
    
    t_end = time.time()

    v = t
    while pre[v[0]][v[1]] != s:
        u = pre[v[0]][v[1]]
        path.append(u)
        map[u[0]][u[1]] = 4
        v = u
        
    return map, searched, path[::-1], t_end - t_start