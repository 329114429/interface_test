from functools import reduce
from operator import mul
from operator import itemgetter
from operator import methodcaller


# 使用reduce函数和匿名函数进行阶乘
def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


# 使用reduce函数和匿名函数进行阶乘
def fact2(n):
    return reduce(mul, range(1, n + 1))


# 按照国家的代码（第二字段）的顺序打印各个城市信息
def test_city():
    metro_data = [('tokyo', 'JP', 36.93, (35.68, 139.691)),
                  ('delhi', 'IN', 21.93, (28.68, 77.691)),
                  ('new york', 'US', 40.93, (40.68, 50.691))]

    city_name = itemgetter(0, 1)  # 构建一个函数，构成一个元组
    city_data = itemgetter(1, 2)

    for city in metro_data:
        print(city_name(city))
        print(city_data(city))
        print("---")


# 使用methodcaller函数
def test_methodcaller():
    str_test = 'hao suo zhong'
    # upcase = methodcaller('upper')  # 创建operator模块下的一个任意方法函数
    # upcase = methodcaller('replace', ' ', '-')
    upcase = methodcaller('replace', ' ', '+')
    print(upcase(str_test))


def main():
    # num = fact2(3)
    # print(num)

    # 按照国家的代码（第二字段）的顺序打印各个城市信息
    # test_city()

    # 创建operator模块下的一个方法函数
    test_methodcaller()


if __name__ == '__main__':
    main()
