# 8.2.2 关键字实参
# def describe_pet(animal_type, pet_name):
#     """显示动物类型，名字"""
#     print("类型：" + animal_type, "姓名：" + pet_name)
#
#
# describe_pet("hao", "suo")
#
# describe_pet(animal_type="老鼠", pet_name="harry")
#
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + middle_name + last_name
#     else:
#         full_name = first_name + last_name
#     return full_name
#
#
# name = get_formatted_name("hao", "suo")
# print(name)
#
# name2 = get_formatted_name("hao", "suo", "zhong")
# # print(name2)
#
# def build_name(first_name, last_name, age=""):
#     """返回一个字典"""
#     fullname = {
#         'firstname': first_name,
#         'lastname': last_name,
#     }
#     if age:
#         fullname['age'] = age
#     return fullname
#
#
# #
# # name = build_name("hao", "suo", "12")
# # print(name)
#
# while True:
#     first = input("first:")
#     last = input("last:")
#     fullname = build_name(first, last)
#     if first == "q" or last == "q":
#         break
#     print(fullname)


def print_models(unprinted_designs, completed_models):
    """模拟打印"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(current_design)
        completed_models.append(current_design)
    return completed_models


def show_completed_models(completed_models):
    unprinted_designs = ["hao", "suo", "zhong"]
    show_completed = print_models(unprinted_designs[:], completed_models)
    for show in show_completed:
        print(show)
    print("原来:", unprinted_designs)
    return show_completed


if __name__ == '__main__':
    completed_models = []
    show_completed_models(completed_models)
