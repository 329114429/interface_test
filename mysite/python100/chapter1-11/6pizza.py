import python100.day01_15.day02 as day


# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }
#
# # for topping in pizza['toppings']:
# #     print(topping)
#
# for name, value in pizza.items():
#     # print(name + str(value))
# #     for va in value:
# #         print(name + va)
#
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     }
#
# }
# for username, user_info in users.items():
#     print('username:' + username)
#     print("full_name " + user_info['first'] + user_info['last'])

#
# def make_pizza(size, *toppings):
#     """打印顾客点的所有配件"""
#     print(toppings)
#     for topping in toppings:
#         print(str(size) + "-" + topping)
#
#
# make_pizza(16, 'peperoni')
# make_pizza(18, 'mushrooms', 'green pepper', 'extra cheese')

def build_profile(first, last, **user_info):
    """创建一个字典"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_info = build_profile('albert', 'einstein', location='princeton')
print(user_info)
