import sys
import unicodedata
import string


def test_sum(a, b):
    c = int(a) + int(b)
    return c


def shave_marks(txt):
    # 去掉全部变音符号
    norm_text = unicodedata.normalize('NFD', txt)
    shaved = "".join(c for c in norm_text if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


# 排序
def reverse_words(words):
    word_list = sorted(words, key=lambda x: len(x))  # 按元素的长度排序
    print(word_list)


def main():
    words = ["sad", "haosuo", "qwda"]
    reverse_words(words)


if __name__ == '__main__':
    main()