from python100.chapter11.name_function import get_formatted_name

print("enter q to quit")
while True:
    first = input("\n first name :")
    if first == 'q':
        break
    last = input("\n last name :")
    if last == 'q':
        break
    full_name = get_formatted_name(first, last)
    print("fullname : " + full_name)
