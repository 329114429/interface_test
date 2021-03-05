"""
接口回帖的配置信息
"""
import json


class SettingThreadReply():
    # 回帖配置信息
    def get_headers(self):
        headers = {
            "host": "www.xiziquan.com",
            "dhash": "bff6ce6d0e2c75f9675f91e4c5c6a594",
            "if-none-match": "",
            "if-modified-since": "",
            "last-modified": "",
            "content-type": "application/x-www-form-urlencoded",
            "content-length": "613",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.11.0"
        }
        return headers

    def get_body(self, params):
        params = json.dumps(params)
        body = {
            "data": params,
            "openid": "e70d97c94e0a34c9c5268d361353de1b",
            "xzkey": "9f62e194b7dc1b6fa66cac86197a5852",
            "version": "5.1.1",
            "token": "c31faddc5316d8641bfff896792deb2e",
            "random": "3ad79cabc3a534ab82960050ff4bb65b15a24ee311d910c17b1216a863d66bf5fc820dd9b0b71548223fe324de5a7281",
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
