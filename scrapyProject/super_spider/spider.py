#  pip install requests beautifulsoup4 selenium opencv-python numpy 
# pip install -i https://mirrors.aliyun.com/pypi/simple/ requests beautifulsoup4 selenium opencv-python numpy

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time
from selenium.common.exceptions import WebDriverException
import re
import cv2
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random

# 随机 User-Agent 列表
# USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/78.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
# ]
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]


service = Service(r'D:\ChromeDriver\chromedriver-win64\chromedriver.exe')
chrome_options = Options()
random_user_agent = random.choice(USER_AGENTS)
chrome_options.add_argument(f'user-agent={random_user_agent}')
# chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
chrome_options.add_argument('--ignore-certificate-errors')

url = "https://bulletin.cebpubservice.com/xxfbcmses/search/bulletin.html?dates=300&categoryId=88&page=1&showStatus=1"
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get(url)
    time.sleep(5)
    page = driver.page_source

    soup = BeautifulSoup(page, 'html.parser')
    td = soup.select('td a')
    for td_a in td:
        link = td_a.get('href')
        link_text = td_a.text.strip()
        print(f"link: {link}")
        print(f"text: {link_text}")

        with open('output.md', 'w', encoding='utf-8') as md_file:
            md_file.write(f"原始链接： {link}\n")
            md_file.write(f"标题： {link_text}\n")

        time.sleep(10)

        if link and link.startswith('javascript:urlOpen('):
            # 用 正则表达式 提取 ID 参数    
            match = re.search(r"javascript:urlOpen\('([^']+)'\)", link)
            if match:
                id_param = match.group(1)
                # opoen 函数生成 link
                normal_link = f'https://ctbpsp.com/#/bulletinDetail?uuid={id_param}&inpvalue=&dataSource=0&tenderAgency='
                print (f"正常链接： {normal_link}")
                md_file.write(f"正常链接：  {normal_link}\n\n")


                # 打开新页面
                driver.get(normal_link)
                time.sleep(10)

                iframe_css_selector = 'iframe[src*="https://i-cn.vaptcha.com/cn/p-test-vip.html?v=1.0.22"]'
                img_css_selector = '#vaptcha > div > div.vp-code > div.vp-main-bg > canvas'
                intelligent_verification_code_page(iframe_css_selector, img_css_selector)

                # def intelligent_verification_code_page(iframe_css_selector, img_css_selector):
                #     iframe_css_selector = 'iframe[src*="https://i-cn.vaptcha.com/cn/p-test-vip.html?v=1.0.22"]'
                #     img_css_selector = '#vaptcha > div > div.vp-code > div.vp-main-bg > canvas'

                #     try:
                #         iframe = WebDriverWait(driver, 10).until(
                #             EC.presence_of_element_located((By.CSS_SELECTOR, iframe_css_selector))
                #         )
                #         driver.switch_to.frame(iframe)

                #         captcha_img= WebDriverWait(driver, 10).until(
                #             EC.presence_of_element_located((By.CSS_SELECTOR, img_css_selector))
                #         )
                #         print("找到图片")
                #     except Exception as e:
                #         print(f"图片没找到： {e}")

                #     # 获取页面的滚动位置
                #     scroll_x = driver.execute_script("return window.pageXOffset;")
                #     scroll_y = driver.execute_script("return window.pageYOffset;")

                #     new_page = driver.page_source
                #     # new_soup = BeautifulSoup(new_page, 'html.parser')
                #     # 定位图片
                #     # captcha_img = driver.find_element('css selector', '#vaptcha > div > div.vp-code > div.vp-main-bg > canvas')
                #     captcha_img = driver.find_element(By.CSS_SELECTOR, img_css_selector)
                #     location = captcha_img.location
                #     size = captcha_img.size
                #     left = location['x']
                #     top = location['y']
                #     right = left + size['width']
                #     bottom = top + size['height']

                #     # 截取图片
                #     driver.save_screenshot('screenshot.png')
                #     screenshot = cv2.imread('screenshot.png')
                #     captcha = screenshot[top: bottom, left: right]
                #     length = len(captcha.shape)
                #     print (f"长度： {length}")

                #     # 检查图像通道数
                #     if  len(captcha.shape)== 3:    # 彩色图像 3 通道
                #         gray = cv2.cvtColor(captcha, cv2.COLOR_BGR2GRAY)   # 彩色图像转换为 灰度图
                #     else:
                #         gray = captcha  # 已经是灰度图，直接使用

                #     # 图像预处理
                #     gray = cv2.cvtColor(captcha, cv2.COLOR_BGR2GRAY)
                #     _,binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

                #     # 查找轮廓
                #     contours,_= cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                #     # 选择最大轮廓
                #     if contours:
                #         max_contours = max(contours, key=cv2.contourArea)
                #         points = []
                #         for point in max_contours:
                #             x,y = point[0]
                #             # 转换为相对于整个页面的坐标
                #             global_x = left+x
                #             global_y = top+y
                #             points.append((global_x, global_y))
                        
                #         # 模拟鼠标轨迹
                #         actions = ActionChains(driver)
                #         actions.move_to_element(captcha_img).move_by_offset(points[0][0] - left, points[0][1] - top)
                #         actions.click_and_hold()
                #         for point in points[1:]:
                #             actions.move_by_offset(*point)
                #         actions.release()
                #         actions.perform()

                #         time.sleep(10)




   

        

except WebDriverException as e:
    print(f"错误：{e}")
finally:
    driver.quit()












