"""
接口发帖的配置信息
"""
import json


class SettingThreadPost():
    # 发帖请求配置
    def get_headers(self):
        headers = {
            "host": "www.xiziquan.com",
            "dhash": "bff6ce6d0e2c75f9675f91e4c5c6a594",
            "if-none-match": "",
            "if-modified-since": "",
            "last-modified": "",
            "content-type": "application/x-www-form-urlencoded",
            "content-length": "643",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.11.0"
        }
        return headers

    def get_body(self, params):
        params = json.dumps(params)

        body = {
            "data": {params},
            "openid": "e70d97c94e0a34c9c5268d361353de1b",
            "xzkey": "cb60d40e7dd0aa6e868b2708140bd66b",
            "version": "5.1.1",
            "token": "c31faddc5316d8641bfff896792deb2e",
            "random": "597c44e2bdbffb175200a447c9d096a99988c1ac278c42a64d5d0423c5f3e325cd446d776d61b985ff2a824ce46aa78b",
            "uid": "2253035",
            "po_token": "035c28e6f10652991f65807ad61b836e",
            "system_type": "2",
            "isdev": "0",
            "device_code": "X/fD5Hhib/EDAMaru45+thvy",
            "device_token": "AsE9h2rjZ5Fh7ruyTpntDER6oT2BhkLIGzhtLdArwWBR",
            "po_uid": "128747",
            "app_id": "1",
            "device": "PBCM30"
        }
        return body
