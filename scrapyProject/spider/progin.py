import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import random
from faker import Faker

# 初始化Faker
fake = Faker()

def generate_random_proxy_ip():
    return fake.ipv4()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

# 设置代理
def set_selenium_driver_proxy(driver_path):
    # random_proxy_ip = generate_random_proxy_ip()
    random_user_agent = get_random_user_agent()

    chrome_options = Options()
    chrome_options.add_argument(f'user-agent={random_user_agent}')
    # 修正代理服务器格式
    # chrome_options.add_argument(f'--proxy-server=http://{random_proxy_ip}')

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


url = 'https://www.proginn.com/works'
driver_path = r'C:\ChromeDriver\chromedriver-win64\chromedriver.exe'

def get_page_resource(url):
    driver = set_selenium_driver_proxy(driver_path)

    try:
        driver.get(url)
        time.sleep(10)
    except Exception as e:
        print(f"访问网站时出错: {e}")
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    items = soup.find_all('div', class_='ma-works-item-tit')
    for item  in items:
        a_tags = item.select('a')
        for a in a_tags:
            a_link = a.get('href')
            a_text = a.text

            with open('./spider/scraped_data.md', 'w', encoding='utf-8') as md_file:
                md_file.write(f"标题： {a_text}\n")
                md_file.write(f"Link: {a_link}")



    img_folder = './spider/downloaded_imgs/'
    os.makedirs(img_folder, exist_ok=True)

get_page_resource(url=url)