from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(executable_path=(r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"), chrome_options=chrome_options)
driver = webdriver.Chrome()
driver.maximize_window()

url = "https://sit1home.uuabc.com/"
driver.get(url)
driver.implicitly_wait(30)

# driver.find_element_by_class_name("btu").click()
time.sleep(4)
driver.find_elements_by_class_name("btn")[2].click()
time.sleep(2)
driver.back()
time.sleep(1)
driver.find_elements_by_class_name("btu")[1].click()
time.sleep(2)
driver.back()
time.sleep(1)
driver.find_elements_by_class_name("btu")[0].click()
time.sleep(2)
driver.back()
# print(element)

# time.sleep(4)
# driver.find_element_by_link_text("U世界").click()
# time.sleep(2)
# driver.back()
# time.sleep(1)
# driver.find_element_by_link_text("直播课").click()
# time.sleep(2)
# driver.back()
# time.sleep(1)
# driver.find_element_by_link_text("登录").click()
# time.sleep(2)
# driver.back()
# time.sleep(1)


# print(element)
# for i in element:
# 	print(i.text)


time.sleep(1)
driver.quit()
