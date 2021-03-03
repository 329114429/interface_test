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
            {
                "fid": self.fid,
                "mode": self.mode,
                "phonetype": self.phonetype,
                "title": self.title,
                "content": self.content
            }
        }
        body = SettingThreadPost().get_body(params=params)

        response = requests.post(self.url, self.headers, data=body)
        response_dict = json.loads(response.text)
        return response_dict
