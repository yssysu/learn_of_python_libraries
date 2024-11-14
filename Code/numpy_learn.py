import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


a1 = np.array([[1,2,3,4,5,6],
                [3,5,7,9,0,8],
                [1,2,3,4,5,6]])

a2 = np.array([[[1, 2, 3, 4, 5, 6],
                [3, 5, 7, 9, 0, 8],
                [1, 2, 3, 4, 5, 6]]])

print(a1.shape)
print(a2.shape)

print(a1)
print(a1[0][2])
print(a1[0][5])

# 提取x, y, z坐标
x = a1[0][0]
y = a1[0][1]
z = a1[0][2]

# 创建一个包含三维坐标轴的图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维点
ax.scatter(x, y, z, c='r', marker='o')  # 使用红色圆点表示

# 设置坐标轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 显示图形
plt.show()

if __name__ == '__main__':
    n = int(input().strip())
    if n / 2 != 0 :
        print('Weird')
    elif  2 <= n and n <= 5 : print('Not Weird')

    elif 6 <= n and n <= 20 : print('Weird')
    elif n > 20: print('Weird')


