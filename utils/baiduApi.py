# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5

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
    return result


# baiduTranslate()
#
# # Show response
# print(json.dumps(result, indent=4, ensure_ascii=False))