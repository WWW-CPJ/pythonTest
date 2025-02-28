import requests 
import unittest
import json
from concurrent .futures import ThreadPoolExecutor

# BASR_URL = 'https://jsonplaceholder.typicode.com'

# TOKEN = 'Bearer YOUR_ACCESS_TOKEN'
# USER = 'your_usename'
# PASSWORD = 'your_password'

# 流式响应
url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
data = {
    "model": "generalv3.5",
    "messages": [
        {
            "role": "user",
            "content": "你是谁"
        }
    ],
    "stream": True
}
header = {
    "Authorization": "Bearer ZsVZwqXWphaMHOtMdVlM:ovLabSODRfzHpJKItiMb"
}
response = requests.post(url, headers=header, json=data, stream=True)

# 流式响应解析示例
response.encoding = "utf-8"
for line in response.iter_lines(decode_unicode="utf-8"):
    print(line)