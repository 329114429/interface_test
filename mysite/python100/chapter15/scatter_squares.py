import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, edgecolors="none", c=y_values, cmap=plt.cm.Blues,
            s=10)  # color 三个数值在 0~1 之间

# 设置图标标题 坐标轴 标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=24)

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig("square_plot.png", bbox_inches='tight') # di

plt.show()
