
import numpy as np

if __name__ == '__main__':
    #-5 到5 线性插值  5j 表示要5个
    x1, x2 = np.mgrid[-5:5:5j, -5:5:5j]
    #axis=2 轴=2
    x = np.stack((x1, x2), axis=2)
    print(x1)
    print(x2)
    print(x)
