"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""

# f = float(input("输入华氏温度: "))
# c = (f - 32) / 1.8
# print("%.1f华氏温度 = %.1f设施温度" % (f, c))


def is_leap(year):
    year = int(year)
    if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
        print("闰年")
    else:
        print("平年")


if __name__ == '__main__':
    is_leap(2020)