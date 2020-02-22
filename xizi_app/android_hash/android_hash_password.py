# android 添加hash值

import hashlib


def str_encrypt(str):
    """
      使用sha1加密算法，返回str加密后的字符串
      """
    sha = hashlib.sha1(str.encode("utf-8"))
    encrypts = sha.hexdigest()
    print(encrypts)
    return encrypts


if __name__ == '__main__':
    path = "/Users/hao/PycharmProjects/xizi_app/android_hash/1xizihupan_v4.16.0.apk"
    str_encrypt(path)

    # 308fef3b132ea948a439f39054644182e989f03f
    # d469b5a4cc67baef88ede3af4c92f414d644e9dc

    # a9205a43e9e523430036385578588b77896775a1
