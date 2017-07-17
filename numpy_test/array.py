import numpy as np

A = np.array([[1.0,1.0,0.0],[0.0,1.0,1.0],[1.0,0.0,1.0]])
Q = np.zeros_like(A)
m = np.shape(Q)[0]
n = np.shape(Q)[1]
cnt = 0

for a in A.T:
    u = np.copy(a)
    for i in range(0, cnt):
        u -= np.dot(np.dot(Q[:, i].T, a), Q[:, i]) # 减去待求向量在以求向量上的投影
    e = u / np.linalg.norm(u)  # 归一化
    Q[:, cnt] = e
    cnt += 1
print (Q)

