# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import random
from hashlib import md5
import requests

API_KEY = "sKQ7uMd160I5D27cq0TiSGup"
SECRET_KEY = "yEbxjq7ch02iAlMv03fpcvLGt2UkGGml"

# Set your own appid/appkey.
appid = '20230507001669070'
appkey = 'fXvMGSqVYDd9IkDspIzf'

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`

lang_dict = {
    "AUTO": "auto",
    "简体中文": "zh",
    "英语": "en",
    "繁体中文": "cht",
    "日语": "jp",
    "粤语": "yue"
}
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path


# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def baiduTranslate(source, target, query):
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    from_lang = lang_dict[source]
    to_lang = lang_dict[target]
    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    print(result)
    return result


def main():
    url = "https://tsn.baidu.com/text2audio"
    text = "你好北京".encode("utf-8")

    payload = f'tex={text}&tok=' + get_access_token() + '&cuid=2121242342343&ctp=1&lan=zh'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response.encoding = "utf-8"
    print(response.headers.get("Content-Type"))
    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
