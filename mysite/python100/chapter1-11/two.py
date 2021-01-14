# 2.3.1
# name = "ada hao"
# print(name.title())
# print(name.upper())
# print(name.lower())
#
# print("===\nhao")
#
# # 删除空白
# message = " 123 "
# print(message.rstrip())  # 删除右边空白
# print(message)
#
# print(message.strip())  # 删除两边空白
#
#
# name = "haosuozhong"
# print(name.title())
# print(name.lower())
# print(name.upper())

# 2.4.0
# age = 23
# message = "happy" + str(age)+ "birthday"
# print(message)
#
# print(1/3)  # 除法
# print(1%3)  # 取余
# print(1//3) # 取整
#
#
# list1 = ['hao', 'suo', 'zhong']
# print(list1[-1])
# list1.insert(1,'zs')
# print(list1)
# print(list1.remove('hao'))
# print(list1)
# list1.sort(reverse=True)
# sorted(list1, reverse=True)
# print(list1)
# print(len(list1))


# # 4.3.1
# for value in range(1,5):
#     print(value)

#
# numbers = list(range(1, 5, 2))
# print(numbers)

#
# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)
#
# min_num = min(squares)
# print(min_num)
#
# squares_1 = [value ** 2 for value in range(1, 5)]
# # print(squares_1)
#
# squares_2 = [value for value in range(1, 10)]
# # # print(squares_2[0:3])
# # # print(squares_2[-2:])
# # # squares_3 = squares_2[:]
# # squares_3 = squares_2
# # squares_2.append(11)
# # squares_3.append(12)
# # print(squares_2)
# # print(squares_3)
#
#
# age = 1
# age2 = 2
# if age > 1 or age2 >2:
#     print("hao")
# else:
#     print("suo")

# if 1 in squares_2:
#     print(age)
# else:
# #     print(age2)
#
# # if 1 not in squares_2:
# #     print(age)
# # else:
# #     print(age2)
#
# if age > 2:
#     print(age)
# elif age > 1:
#     print(age2)
# else:
#     print("hao")
#

# # 5.3.3
# age = 66
# if age < 4:
#     print("免费")
# elif age < 18:
#     print("5")
# elif age < 50:
#     print("老人")
# else:
#     print("18")
#

# num_list1 = [value for value in range(1, 10)]
# num_list2 = [value for value in range(1, 5)]
#
# for num in num_list1:
#     if num in num_list2:
#         print("num1:" + str(num))
#     else:
#         print("num2:" + str(num))
# # print(num_list1)
# #
#
# # 6.0.0
#
# aline_0 = {
#     'x_position': 0,
#     'y_position': 25,
#     'speed': 'medium',
# }
#
# if aline_0['speed'] == 'slow':
#     x_increment = 1
# elif aline_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0 = {
#     'color': 'green',
#     'points': 5,
#
# }
#
# del alien_0['points']
# print(alien_0)

user_0 = {
    'username': 'hao',
    'first': 'suo',
    'last': 'zhong',
    'last1': 'hao',
}

# for key, value in user_0.items():
#     print(key)
#     print(value)

# for key in user_0.keys():
#     print(key.title())
#     if key == "last":
#         print("haosuozhong")
#
# for key in sorted(user_0.keys()):
#     print(key)

# for value in sorted(user_0.values()):
#     print(value)

# for value in sorted(set(user_0.values())):
#     print(value)
#
#
aliens = []
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    if alien['color'] == 'yellow':
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)

print("Total number of aliens :" + str(len(aliens)))
