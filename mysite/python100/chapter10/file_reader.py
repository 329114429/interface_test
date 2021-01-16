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

filename = "hao.txt"

try:
    with open(filename) as file:
        contents = file.read()
except FileNotFoundError:
    msg = "not file"
    print(msg)
