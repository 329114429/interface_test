import pygal

from python100.chapter15.die import Die

# 创建一个die
die = Die()
die_2 = Die(10)

# 骰子几次，并将结果存在一个列表中
results = []
for roll_number in range(100):
    result = die.roll() + die_2.roll()
    results.append(result)
#
# print(results)

# 分析结果
frequencies = []
max_result = die.num_sides + die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 对结果可视化
hist = pygal.Bar()

hist.title = "results of rolling one D6 100 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequencies of results"

hist.add("D6+D6", frequencies)
hist.render_to_file('die_visual.svg')
