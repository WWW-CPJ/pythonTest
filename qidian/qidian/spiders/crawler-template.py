import requests 
from bs4 import BeautifulSoup

#发送 http 请求 获取网页内容
url = 'http://zh.wikipedia.org/zh-cn/Main_Page'
response = requests.get(url)
html_content = response.text

#使用beautifulsoup 解析 html
soup = BeautifulSoup(html_content, 'html.parser')

# 提取标题和首段内容
title = soup.find('h1', id='firstHeading').text
first_paragraph = soup.find('div', id = 'mf-art').text


print("标题：", title)
print("首段内容：", first_paragraph)
