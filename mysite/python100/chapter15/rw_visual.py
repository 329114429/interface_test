import sys
sys.path.append(".")

from python100.chapter15.random_walk import RandomWalk
import matplotlib.pyplot as plt

# 创建一个RandomWalk实例
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 绘制窗口尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,
                rw.y_values,
                c=point_numbers,
                cmap=plt.cm.Blues,
                edgecolors='none',
                s=10)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1],
                rw.y_values[-1],
                c='red',
                edgecolors='none',
                s=100)

    # 隐藏坐标轴, 会警告，绘制图之前定义了标题和刻度
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)

    plt.show()

    keep_running = input("Make another walk y/n : ")
    if keep_running == "n":
        break
