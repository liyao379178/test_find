from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
import time
import random

# 设置chrome为手机浏览模式，deviceName就是手机型号
mobileEmulation = {"deviceName": "iPhone 5/SE"}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe',
						  chrome_options=options)
# driver = webdriver.Chrome( chrome_options=options)

username = "1470000"+''.join(random.sample('1234567890',8))

driver.get("https://www.uuabc.com/index.html")
# 输入账号
driver.find_element_by_id("experience-head1").click()
time.sleep(1)
# driver.find_element_by_id("username").send_keys("username")
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("passwd")
user = driver.find_elements_by_class_name("textarea")[0]
user.send_keys(username)
time.sleep()


sleep(3)
# 点击登录按钮
doc = driver.find_element_by_id("login")
TouchActions(driver).tap(doc).perform()
sleep(3)
driver.quit()
