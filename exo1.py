import numpy as np
import matplotlib.pyplot as plt
import math


def curves(n: int):
    plt.plot(np.array([i for i in range(1,n)]))
    plt.plot(np.array([math.log(i) for i in range(1,n)]))
    plt.plot(np.array([pow(i,2) for i in range(1,n)]))
    plt.plot(np.array([pow(2,i) for i in range(1,n)]))
    plt.plot(np.array([i * math.log(i) for i in range(1,n)]))
    plt.legend(["n","log(n)","n²","2^*n","n log(n)"])
    plt.show()
    plt.savefig("result.png")


curves(5)