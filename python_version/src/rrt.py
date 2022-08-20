import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as mla
import random

def cal_area(points):
    x = [i[0] for i in points]
    y = [i[1] for i in points]
    s = 0
    n = len(x)
    for i in range(n):
        s += x[i]*y[(i+1)%n] - x[i]*y[(i-1)%n]
    s /= 2
    return np.abs(s) 

def inside(point, polygon):
    s1 = cal_area(polygon)
    s2 = 0.0
    n = len(polygon)
    for i in range(n):
        s2 += cal_area([point, polygon[i], polygon[(i+1)%n]])
    return np.abs(s1-s2)<1e-3

def cross(start, end, polygon, n):
    v_u = (end - start) / n
    v0 = start
    for i in range(n+1):
        if inside(v0, polygon):
            return True
        v0 += v_u
    return False

def rand_state(p, goal, x_min, x_max, y_min, y_max, obs):
    if random.uniform(0,1) < p:
        return np.array(goal)
    else:
        v = np.array((random.uniform(x_min, x_max), random.uniform(y_min, y_max)))
        flag = False
        for i in obs:
            flag |= inside(v, i)
        while flag:
            v = np.array((random.uniform(x_min, x_max), random.uniform(y_min, y_max)))
            flag = False
            for i in obs:
                flag |= inside(v, i)
        return v

def nearest_neigbour(vertice, goal):
    i = int(np.argmin([math.hypot(vertex[0]-goal[0], vertex[1]-goal[1]) for vertex in vertice]))
    return vertice[i], i
    

def new_state(v_near, v_rand, step, obs):
    flag = True
    dis = np.linalg.norm(v_rand-v_near)
    v_new = np.array([-1,-1])
    if dis == 0:
        return False, v_new
    v_new = (v_rand-v_near) / dis * min(dis, step) + v_near
    for i in obs:
        if cross(v_near, v_new, i, 5):
            flag = False
            break
    return flag, v_new
    
    
x_init, y_init = 10.0, 10.0
x_goal, y_goal = 40.0,40.0
x_new, y_new = x_init, y_init
v_init = np.array((x_init, y_init))
v_goal = np.array((x_goal, y_goal))
p = 0.3
step = 1 # the program will want wrong when the step is longer, i don't know why
tol = 1
N = 10000

obstacle1 = [np.array((5,5)), np.array((5,45)), np.array((6,45)),np.array((6,5))]
obstacle2 = [np.array((6,44)), np.array((6,45)), np.array((45,45)),np.array((45,44))]
obstacle3 = [np.array((44,44)), np.array((45,44)), np.array((45,5)),np.array((44,5))]
obstacle4 = [np.array((45,5)), np.array((5,5)), np.array((5,6)),np.array((45,6))]
obstacle5 = [np.array((17,27)), np.array((18,27)), np.array((18,6)),np.array((17,6))]
obstacle6 = [np.array((30,20)), np.array((40,20)), np.array((40,19)),np.array((30,19))]
obstacle7 = [np.array((35,44)), np.array((36,44)), np.array((36,20)),np.array((35,20))]
obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7]

fig, ax = plt.subplots()
ax.set_aspect(1)
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)

for obstacle in obstacles:
    x = [i[0] for i in obstacle]
    y = [i[1] for i in obstacle]
    plt.fill(x, y, color="black")


v = [v_init]
edges = []
fa = [-1]

plt.scatter(x_init, y_init, color='red')
plt.scatter(x_goal, y_goal, color='blue')

while np.linalg.norm(v[-1]-v_goal) > step and N:
    v_rand = rand_state(p, v_goal, 5, 44, 5, 44, obstacles)
    v_near, ind = nearest_neigbour(v, v_rand)
    v_copy = v_near.copy()
    flag, v_new = new_state(v_near.copy(), v_rand, step, obstacles)
    if not flag:
        continue
    N -= 1
    v.append(v_new)
    fa.append(ind)
    edges.append((v_copy, v_new))
    print(N)

edges.append((v[-1], v_goal))
fa.append(len(v)-1)
v.append(v_goal)
E = len(edges)
print("finish")
# recover the path
p = []
ind = len(v)-1
while fa[ind] > 0:
    p.append((v[ind], v[fa[ind]]))
    ind = fa[ind]
p = p[::-1]

# save the progress as gif
n = len(edges)
m = len(p)
edges += p
def update(frame):
    e = edges[frame]
    v1 = e[0]
    v2 = e[1]
    plt.plot([v1[0], v2[0]], [v1[1], v2[1]], color="green" if frame < n else "red")

pw_writer = mla.PillowWriter(fps=50)
for i in range(n+m):
    update(i)
    plt.pause(0.00001)
