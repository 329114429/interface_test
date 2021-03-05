"""
实现回帖接口的验证
"""
import requests
import json
from config.thread_reply_setting import SettingThreadReply


class ApiThreadReply():
    # 回帖类
    def __init__(self, url, phonetype, quoteusername, tid, content):
        self.url = url
        self.phonetype = phonetype
        self.quoteusername = quoteusername

        self.tid = tid
        self.content = content
        self.headers = SettingThreadReply().get_headers()

    def thread_reply(self):
        # 回帖方法
        params = {
            "params": {
                "phonetype": self.phonetype,
                "quoteusername": self.quoteusername,
                "tid": self.tid,
                "content": self.content
            }
        }
        body = SettingThreadReply().get_body(params)
        response = requests.post(self.url, headers=self.headers, data=body)
        response_dict = json.loads(response.text)
        print(response_dict)


if __name__ == '__main__':
    url = "https://www.xiziquan.com/index.php?r=thread/reply&v=4.2.1"
    phonetype = 1
    quoteusername = "jiushitiao"
    tid = 4882932
    content = "删除"
    a = ApiThreadReply(url, phonetype, quoteusername, tid, content).thread_reply()
    print(a)
