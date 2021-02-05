import pygal

from python100.chapter15.die import Die

# 创建一个die
die = Die()

# 骰子几次，并将结果存在一个列表中
results = []
for roll_number in range(100):
    result = die.roll()
    results.append(result)
#
# print(results)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 对结果可视化
hist = pygal.Bar()

hist.title = "results of rolling one D6 100 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequencies of results"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')