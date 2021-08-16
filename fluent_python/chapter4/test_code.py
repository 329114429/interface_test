import sys


def test_sum(a, b):
    c = int(a) + int(b)
    return c


if __name__ == '__main__':
    c = test_sum(2, 3)
    print(c)
