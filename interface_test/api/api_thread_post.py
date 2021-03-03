"""
实现发帖接口的验证
"""

import requests


class ThreadPost():
    # 发布帖子类
    def __init__(self, mode, title, content):
        self.mode = mode
        self.title = title
        self.content = content


