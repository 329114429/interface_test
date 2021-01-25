import base64

with open("/Users/hao/PycharmProjects/mysite/haotest/2020_10.png", "rb") as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    print('data:images/jpeg;base64, %s' % s)
    f.close()

