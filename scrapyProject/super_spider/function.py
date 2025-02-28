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


def intelligent_verification_code_page(iframe_css_selector, img_css_selector):
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, iframe_css_selector))
        )
        driver.switch_to.frame(iframe)

        captcha_img= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, img_css_selector))
        )
        print("找到图片")
    except Exception as e:
        print(f"图片没找到： {e}")

    # 获取页面的滚动位置
    scroll_x = driver.execute_script("return window.pageXOffset;")
    scroll_y = driver.execute_script("return window.pageYOffset;")

    new_page = driver.page_source
    # new_soup = BeautifulSoup(new_page, 'html.parser')
    # 定位图片
    # captcha_img = driver.find_element('css selector', '#vaptcha > div > div.vp-code > div.vp-main-bg > canvas')
    captcha_img = driver.find_element(By.CSS_SELECTOR, img_css_selector)
    location = captcha_img.location
    size = captcha_img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    # 截取图片
    driver.save_screenshot('screenshot.png')
    screenshot = cv2.imread('screenshot.png')
    captcha = screenshot[top: bottom, left: right]
    length = len(captcha.shape)
    print (f"长度： {length}")

    # 检查图像通道数
    if  len(captcha.shape)== 3:    # 彩色图像 3 通道
        gray = cv2.cvtColor(captcha, cv2.COLOR_BGR2GRAY)   # 彩色图像转换为 灰度图
    else:
        gray = captcha  # 已经是灰度图，直接使用

    # 图像预处理
    gray = cv2.cvtColor(captcha, cv2.COLOR_BGR2GRAY)
    _,binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 查找轮廓
    contours,_= cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 选择最大轮廓
    if contours:
        max_contours = max(contours, key=cv2.contourArea)
        points = []
        for point in max_contours:
            x,y = point[0]
            # 转换为相对于整个页面的坐标
            global_x = left+x
            global_y = top+y
            points.append((global_x, global_y))
        
        # 模拟鼠标轨迹
        actions = ActionChains(driver)
        actions.move_to_element(captcha_img).move_by_offset(points[0][0] - left, points[0][1] - top)
        actions.click_and_hold()
        for point in points[1:]:
            actions.move_by_offset(*point)
        actions.release()
        actions.perform()

        time.sleep(10)
