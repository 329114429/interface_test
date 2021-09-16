import random


# 排序函数,按列表元素的长度进行排序
def reverse_words(words):
    word_list = sorted(words, key=lambda x: len(x))
    print(word_list)


# 提取乱序的列表元素
class BingoCage():
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


def main():
    # words = ["hao", "suozhong", "yuzhi"]
    # reverse_words(words)
    binggo = BingoCage(range(4))
    print(binggo.pick())


if __name__ == '__main__':
    main()