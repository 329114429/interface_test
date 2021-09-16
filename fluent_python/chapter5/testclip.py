# 在指定的长度附近截取字符串的函数
def clip(text: str, max_len=80):
    # 在max_len前面或后面的一个空格处截断文本
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end == None:
        end = len(text)

    return text[:end].tstrip()  # rstrip() 删除 string 字符串 末尾 的指定字符（默认为空格）
