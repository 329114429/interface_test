# 正则表达式

import re

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""


def main0():
    username = input('输入用户:')
    qq = input('输入QQ:')

    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象

    m1 = re.match(r'^[0-9a-zA-Z]{6,20}$', username)
    if not m1:
        print('输入有效名字')

    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('有效QQ')

    if not m1 and m2:
        print('有效信息')


if __name__ == '__main__':
    main0()