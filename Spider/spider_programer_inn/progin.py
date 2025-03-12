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
        driver.quit()
        return
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    list_div = soup.find('div', class_='ma-works-list')
    if not list_div:
        print("未找到 'ma-works-list' div")
        driver.quit()
        return

    items = list_div.find_all('div', class_='ma-works-item')
    for item in items:
        title_items = item.find_all('div', class_='ma-works-item-tit')
        with open('./spider/scraped_data.md', 'w', encoding='utf-8') as md_file:
            for title_item in title_items:
                a_tags = title_item.select('a')
                for a in a_tags:
                    a_link = a.get('href')
                    a_text = a.text.strip()
                    md_file.write(f"标题： {a_text}\n")
                    md_file.write(f"Link: {a_link}\n")

    # 设置图片保存的文件夹路径
    img_folder = './spider/downloaded_imgs/'
    os.makedirs(img_folder, exist_ok=True)  # 如果文件夹不存在，创建它

    img_items= list_div.find_all('img', class_='img')
    for img_item in img_items:
        img_src = img_item.get('src')
        if img_src:  # 如果 src 存在
            img_url = img_src if img_src.startswith('http') else 'https://example.com' + img_src  # 确保完整的 URL

            # 获取图片的文件名
            img_name = os.path.basename(img_url.split('?')[0])  # 获取文件名，去掉查询字符串部分

            # 下载图片并保存
            img_path = os.path.join(img_folder, img_name)
            try:
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    with open(img_path, 'wb') as f:
                        f.write(img_response.content)
                    print(f"图片 '{img_name}' 已下载并保存到 '{img_folder}'")
                else:
                    print(f"无法下载图片: {img_url}")
            except requests.exceptions.RequestException as e:
                print(f"下载图片时发生错误: {e}")

    driver.quit()

get_page_resource(url=url)