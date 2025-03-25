from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


service = Service(r'C:\ChromeDriver\chromedriver-win64\chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-insecure-localhost')   # 允许本地不安全连接
chrome_options.add_argument('--ssl-version-min=tls1.2')  # 强制使用 TLS 1.2+

url = "https://www.cebupacificair.com/zh-CN/"
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # 找到  I agree  并点击
    cookies_div = soup.find('div', class_='cookies ng-tns-c93-4 ng-trigger ng-trigger-default ng-star-inserted')
    if cookies_div:
        # 在找到的 div 元素内查找符合条件的 a 标签
        target_a = cookies_div.find('a', class_='o-btn o-btn--primary-blue ng-tns-c93-4', string='I agree')

        if target_a:
            # 使用 Selenium 定位并点击元素
            selenium_a = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//a[@class="o-btn o-btn--primary-blue ng-tns-c93-4" and text()="I agree"]'))
            )
            selenium_a.click()
            print("成功点击目标 a 标签")
        else:
            print("未在指定 div 下找到符合条件的 a 标签。")
    else:
        print("未找到指定 class 的 div 元素。")

    # 点击 搜索航班
    search_flights_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '搜索航班')]"))
    )
    search_flights_button.click()
    print("点击 搜索航班 ")
    time.sleep(10)


    # 起始站
    start_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/input'))
    )
    print("成功找到目标 start input 标签")
    # 使用JavaScript来清空输入框的值
    start_input.click()

    # x_tag = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/a[2]'))
    # )
    # x_tag.click()
    # driver.execute_script("arguments[0].value = '';", start_input)

    dingweiqi = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/a[1]'))
    )
    dingweiqi.click()
    Philippines = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/ul/li[9]/a'))
    )
    Philippines.click()
    manila = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/ul/li[9]/ul/li[22]/a'))
    )
    manila.click()
    print("成功选择起始站 MNL")

    time.sleep(3)

    # 终点站
    Philippines = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/ul/li[9]/a'))
    )
    Philippines.click()
    print("成功选择  Philippines")
    cebu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/ul/li[9]/ul/li[9]/a'))
    )
    cebu.click()
    print("成功选择终点站 cebu")
    time.sleep(3)

    # 查找 开始时间 
    startdate_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/input'))
    )
    print("成功找到目标 start date 标签")
    startdate_input.click()
    time.sleep(3)

    date_23 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[7]/div[2]/div'))
    )
    date_23.click()
    print("成功选择开始时间")

    time.sleep(10)

     # 查找 结束时间 
    enddate_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/input'))
    )
    print("成功找到目标 end date 标签")
    enddate_input.click()
    time.sleep(3)

    date_30 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[8]/div[2]/div/span'))
    )
    date_23.click()
    print("成功选择结束时间")

    select_data = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[3]/div/button'))
    )
    select_data.click()
    print("成功选择日期")
    time.sleep(10)

    select_flights = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-home/omnix-search-flight-modal/div/div[2]/div[4]/div[2]/button'))
    )
    select_flights.click()
    print("点击搜索航班")

    time.sleep(30)


    # 等待包含指定 class 的元素加载完成
    hangbanxinxi = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ng-tns-c19-47.ng-star-inserted'))
    )

    # 开始时间
    start_time = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-select-flight/section/div[3]/div[4]/div[4]/div[1]/div/div/div[1]/div/div[1]/span[2]'))
    )
    start_time_text = start_time.text
    print(f"出发时间： {start_time_text}")

    end_time = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-select-flight/section/div[3]/div[4]/div[4]/div[1]/div/div/div[1]/div/div[2]/span[1]'))
    )
    end_time_text = end_time.text
    print(f"到达时间： {end_time_text}")

    leng_time = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-select-flight/section/div[3]/div[4]/div[4]/div[1]/div/div/div[1]/div/div[3]/span'))
    )
    leng_time_text = leng_time.text
    print(f"时长： {leng_time_text}")

    tier = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-select-flight/section/div[3]/div[4]/div[4]/div[1]/div/div/div[2]/div[2]/span[2]'))
    )
    tier_text = tier.text
    print(f"价格： {tier_text}")

    flight = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/omnix-project/omnix-main-master-page/div/omnix-select-flight/section/div[3]/div[4]/div[4]/div[1]/div/div/div[1]/div/div[4]/span[1]'))
    )
    flight_text = flight.text
    print(f"航班： {flight_text}")

    # 创建一个包含所有信息的字典
    flight_info = {
        "航班班次": flight_text,
        "出发站点": "Manila MNL",
        "到达站点": "Cebu CEB",
        "出发时间": start_time_text,
        "到达时间": end_time_text,
        "旅途时长": leng_time_text,
        "全包票价/乘客": tier_text
    }

    # 将字典转换为 JSON 字符串
    flight_info_json = json.dumps(flight_info, ensure_ascii=False, indent=4)

    # 输出 JSON 数据
    print(flight_info_json)

    time.sleep(60)
    

except WebDriverException as e:
    print(f"错误：{e}")
finally:
    driver.quit()