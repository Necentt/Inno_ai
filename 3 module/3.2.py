import matplotlib
matplotlib.use('TkAgg')




import numpy as np
import matplotlib.pyplot as plt
b = 3
N = 10
x1 = np.random.random(N)
x2 = x1 + [np.random.randint(N*2)/(N*2) for i in range(N)] + b
C1 = [x1, x2]
x1 = np.random.random(N)
x2 = x1 - [np.random.randint(N*2)/(N*2) for i in range(N)] + b
C2 = [x1, x2]
f = [0 + b, 1+ b]
w1 = -1
w2 = 1
w3 = -b * w2
w = np.array([w1, w2, w3])
plt.scatter(C1[0][:], C1[1][:], c='red')
plt.scatter(C2[0][:], C2[1][:], c='purple')
plt.plot(f)
plt.show()