import json


# file_path = "/Users/hao/PycharmProjects/mysite/python100/python源码/chapter_10/pi_million_digits.txt"

# with open(file_path) as file:
#     contents = file.read()
#     print(contents.rstrip())

# with open(file_path) as file:
#     lines = file.readlines()
#
#
# pi = ''
# for line in lines:
#     pi += line.strip()
#
# birthday = input("birthday:")
# if birthday in pi:
#     print("you birthday in the first million digits of pil")
# else:
#     print("not appear in the million digits of pil")
#
# print(pi[:52])
# print(len(pi))
#
# filename = "programming.txt"
#
# # with open(filename, 'w') as file:
# #     file.write("i love programming .\n")
# #     file.write("i love programming .\n")
#
# with open(filename, 'a') as file:
#     file.write("i love 3 .\n")
#     file.write("i love 4 \n")
#
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print(" you can't")
#
#
#
# print("two number")
# print("enter q to quit")
#
# while True:
#     first_number = input("first number :")
#     if first_number == "q":
#         break
#     second_number = input("second number :")
#     if second_number == "q":
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("you can't divide by 0 ")
#     else:
#         print(answer)

# filename = "hao.txt"
#
# try:
#     with open(filename) as file:
#         contents = file.read()
# except FileNotFoundError:
#     msg = "not file"
#     print(msg)

# filename = "/Users/hao/PycharmProjects/mysite/python100/python源码/chapter_10/alice.txt"


# def count_words(filename):
#     try:
#         with open(filename) as f:
#             contents = f.read()
#     except FileNotFoundError:
#         # msg = "not exits "
#         # print(msg)
#         pass
#     else:
#         words = contents.split()
#         number_words = len(words)
#         print(number_words)
#
#
# filename = ["/Users/hao/PycharmProjects/mysite/python100/python源码/chapter_10/alice.txt", "hao",
#             "/Users/hao/PycharmProjects/mysite/python100/python源码/chapter_10/little_women.txt"]
# for file in filename:
#     count_words(file)

# numbers = [1, 2, 3, 4, 5]
# filename = 'numbers.json'
# with open(filename, 'w') as f:
#     json.dump(numbers, f)


# filename = "numbers.json"
# with open(filename, 'r') as file:
#     numbers = json.load(file)
#
# print(numbers)

# # username = input("your name:")
# filename = "username.json"
#
# # try:
# #     with open(filename, 'w') as file:
# #         json.dump(username, file)  # 把username写进file
# # except FileNotFoundError:
# #     pass
# # else:
# #     print("come back : " + username)
#
#
# try:
#     with open(filename) as file:
#         username = json.load(file)
# except FileNotFoundError:
#     username = input("your name:")
#     with open(filename, "w") as file:   # 如果没有，就重新写进入
#         json.dump(username, file)
#         print("back" + username)
# else:
#     print("back " + username)


def get_stored_username():
    """获取用户"""
    filename = "/Users/hao/PycharmProjects/mysite/python100/chapter10/username.json"
    try:
        with open(filename) as filename:
            username = json.load(filename)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """获取新用户"""
    username = input("your name:")
    filename = "username.json"
    with open(filename, 'w') as filename:
        json.dump(username, filename)
    return username


def greet_user():
    """问候用户"""
    username = get_stored_username()
    if username:
        print("welcome back :" + username)
    else:
        username = get_new_username()
        print("remember your " + username)


if __name__ == '__main__':
    greet_user()
