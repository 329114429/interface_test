import json


class ReadJson(object):
    # 读取json类
    def __init__(self, filename):
        self.filepath = "./data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)  # 转为字典格式
            return data


if __name__ == '__main__':
    # data = ReadJson("logincode.json").read_json()
    # data = ReadJson("threadpost.json").read_json()
    data = ReadJson("threadreply.json").read_json()
    print(data)

    # for key, value in data.items():
    #     url = value.get("url")
    #     phone = value.get("phone")
    #     ret = value.get("ret")
    #     text = value.get("text")
    #     print(url)
    #     print(phone)
    #     print(ret)
    #     print(text)
