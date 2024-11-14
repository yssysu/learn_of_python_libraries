import math
import random
import matplotlib.pyplot as plt
import numpy as np

# 创建一个2x2的子图网格
fig, axs = plt.subplots(2, 2)

# 遍历axs数组中的每个轴
for ax in axs.flat:  # axs.flat将axs转换为一维迭代器
    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')
    ax.xaxis
for k  in range(2):
    for val in range(2):
        x = []
        y = []
        for i in range(100):
            x.append(random.randint(1, 100))
            y.append(math.sin(x[i]))

        axs[k,val].plot(x,y,linestyle='--',color='black',linewidth=1)
        axs[k,val].scatter(x,y,marker='s',color='red',linewidths=2)

        # axs[k,val].legend(['Line','points'])
        R = 0.5
        G = 0.8
        B = 0.2
        fig.legend(['points','line'],labelcolor = 'black',
                   title = 'extension',markerfirst = True,
                   shadow = True,facecolor = [R,G,B])


plt.show()

