import numpy as np

def dfs(map:np.array,s:tuple,t:tuple,N):
    stack = [s] # the stack to store the vertices
    pre = [[(-1,-1) for i in range(N)] for i in range(N)]
    visited = [[False for i in range(N)] for i in range(N)]
    visited[s[0]][s[1]] = True

    # return value
    searched = []
    path = []

    while stack:
        v = stack.pop()
        v_x = v[0]
        v_y = v[1]
        if v != s:
            map[v_x][v_y] = 3
            searched.append(v)

        # suppose the robot can only move in four directions
        # right
        u = (v_x+1,v_y)
        u_x = u[0]
        u_y = u[1]
        if map[u_x][u_y] == 0 and not visited[u_x][u_y]:
            stack.append(u)
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
            stack.append(u)
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
            stack.append(u)
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
            stack.append(u)
            visited[u_x][u_y] = True
            pre[u_x][u_y] = v
        elif u == t:
            pre[u_x][u_y] = v
            break
    

    # recovery the path
    v = t
    while pre[v[0]][v[1]] != s:
        u = pre[v[0]][v[1]]
        path.append(u)
        map[u[0]][u[1]] = 4
        v = u
    
    return map, searched, path[::-1]

