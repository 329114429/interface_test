"""
实现发帖接口的验证
"""

import requests
import json
from config.thread_post_setting import SettingThreadPost


class ThreadPost():
    # 发布帖子类
    def __init__(self, url, fid, mode, phonetype, title, content):
        self.url = url
        self.fid = fid
        self.mode = mode
        self.phonetype = phonetype
        self.title = title
        self.content = content
        self.headers = SettingThreadPost().get_headers()

    def thread_post(self):
        # 发帖函数方法
        params = {
            "params": {
                "fid": self.fid,
                "mode": self.mode,
                "phonetype": self.phonetype,
                "title": self.title,
                "content": self.content
            }
        }
        body = SettingThreadPost().get_body(params)

        response = requests.post(self.url, headers=self.headers, data=body)
        response_dict = json.loads(response.text)
        return response_dict


if __name__ == '__main__':
    url = "https://www.xiziquan.com/index.php?r=thread/post&v=4.8.0"
    fid = 16
    mode = 1
    phonetype = 1
    title = "找小编删除帖子"
    content = "删除帖子"
    t = ThreadPost(url, fid, mode, phonetype, title, content).thread_post()
    print(t)
