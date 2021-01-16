file_path = "/Users/hao/PycharmProjects/mysite/python100/chapter10/pi_digits"

# with open(file_path) as file:
#     contents = file.read()
#     print(contents.rstrip())

with open(file_path) as file:
    lines = file.readlines()


pi = ''
for line in lines:
    pi += line.strip()

print(pi)
print(len(pi))