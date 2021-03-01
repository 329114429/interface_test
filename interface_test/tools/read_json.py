import json


class ReadJson(object):
    # 读取json类
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data


if __name__ == '__main__':
    data = ReadJson("logincode.json").read_json()
    url = data.get("url")
    phone = data.get("phone")
    ret = data.get("ret")
    text = data.get("text")
    print(url)
    print(phone)
    print(ret)
    print(text)
