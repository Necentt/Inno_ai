import matplotlib
matplotlib.use('TkAgg')


import numpy as np
import matplotlib.pyplot as plt
N = 20
b = 3
x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10)/10 for i in range(N)] + b
C1 = [x1, x2]
x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1 + b
C2 = [x1, x2]
f = [0 + b, 1 + b]
w1 = -0.5
w2 = 0.5
w3 = -b * w2
w = np.array([w1, w2, w3])
for i in range(N):
    x = np.array([C2[0][i], C2[1][i], 1])
    y = np.dot(w, x)
    if y >= 0: print('Класс C1')
    else: print('Класс C2')
plt.scatter(C1[0][:], C1[1][:], c='red')
plt.scatter(C2[0][:], C2[1][:], c='blue')
plt.plot(f)
plt.show()
