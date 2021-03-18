import json


class ReadJson(object):
    # 读取json类
    def __init__(self, filename):
        self.filepath = "/Users/hao/PycharmProjects/interface_test/interface_test/data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)  # 转为字典格式
            return data


if __name__ == '__main__':
    # data = ReadJson("logincode.json").read_json()
    # data = ReadJson("threadpost.json").read_json()
    # data = ReadJson("threadreply.json").read_json()
    # print(data)

    data = ReadJson("logincode_more.json").read_json()
    arrs_list = []
    for key, value in data.items():
        # print(key)
        # print(value)
        arrs_list.append(
            (
                value.get("url"),
                value.get("phone"),
                value.get("ret"),
                value.get("text")
            )
        )
    print(arrs_list)
