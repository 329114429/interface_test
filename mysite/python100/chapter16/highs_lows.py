import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)

    # 返回文件的下一行
    header_row = next(reader)

    # for index, column in enumerate(header_row):
    #     print(index, column)

    # 获取最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])  # 转为数字
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 根据数据描述图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)

    # 图标区着色
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    plt.title("Daily high and low temperatures - 2014", fontsize=14)
    plt.xlabel('', fontsize=16)

    # 绘制斜的日期标签
    fig.autofmt_xdate()

    plt.ylabel("Temperatures(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', size=16)

    plt.show()
