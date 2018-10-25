import numpy as np

data_nd1 = np.loadtxt("ND1_0.csv", delimiter=",")

data_nd3 = np.loadtxt("ND3_0.csv", delimiter=",")

import matplotlib.pyplot as plt

wave = 600.

arg = np.argmin(np.abs(data_nd1[:,0] - wave))

plt.figure()
plt.plot(data_nd3[:,0], data_nd3[:,1]/data_nd3[arg,1], color="blue")
plt.plot(data_nd1[:,0], data_nd1[:,1]/data_nd1[arg,1], color="green")

plt.show()
