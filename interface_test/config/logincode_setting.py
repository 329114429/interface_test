"""
设置基础的配置
"""
import json


class SettingLoginCode():
    # 请求手机配置信息

    def get_headers(self):
        headers = {
            "host": "www.xiziquan.com",
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "gzip",
            "user-agent": "quan/5.1.2 (iPhone; iOS 14.4; Scale/2.00)",
        }

        return headers

    def get_body(self, params):
        params = json.dumps(params)
        body = {
            "app_id": 1,
            "data": {params},
            "device": "iPhone11 ,8",
            "device_code": "3E530EC9-E0E5-4B10-907E-6D4A8ABDD0D8",
            "device_token": "0a9b6ad9a1979d16e9c730f722c44a3cad51f946a9a00329c5f4d32cb33414fe",
            "isdev": 1,
            "random": "e9d67a3093196fa1c84835bec4a6c155",
            "system_type": 1,
            "timestamp": 1614308784,
            "version": "5.1.2",
            "xzkey": "fd10dbf7ea7fec6230a2df7713865e76"

        }
        return body
