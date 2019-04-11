from numpy import *
import numpy as np


def chengmi(ma, v, e, N):
    l0 = 0
    namuda = v.max()
    u = v*(1/namuda)
    for i in range(N):
        print(i)
        v = ma*u
        namuda = max(v)
        if namuda == 0:
            return 0
        u = v*(1/namuda)
        print(namuda, v, u)
        if abs(namuda-l0) < e:
            return namuda, u
        l0 = namuda
    return 0


ma = array([[6, 2, 1], [2, 3, 1], [1, 1, 1]])
a1 = np.mat(ma)
v = array([[1], [1], [1]])
v1 = np.mat(v)
e = 0.001
N = 20
print(chengmi(a1, v1, e, N))
