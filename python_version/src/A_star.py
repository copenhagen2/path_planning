import numpy as np
import queue

def A_star(map:np.array, s:tuple, t:tuple):
    q = queue.PriorityQueue()
    g = [[np.inf for i in range(50)] for i in range(50)]
    f = [[np.inf for i in range(50)] for i in range(50)]
    return map