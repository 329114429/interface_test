from python100.chapter15.random_walk import RandomWalk
import matplotlib.pyplot as plt

# 创建一个RandomWalk实例
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk y/n : ")
    if keep_running == "n":
        break
