"""
接口发帖的配置信息
"""
import json

class SettingThreadPost():
    # 发帖请求配置
    def get_headers(self):
        headers = {

        }

    def get_body(self, params):
        params = json.dumps(params)
        body = {

        }
