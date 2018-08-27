from selenium import webdriver
import random
import time

driver = webdriver.Chrome()
url = "https://www.uuabc.com/Public/newlogin/index.html#/login"
driver.implicitly_wait(30)
driver.maximize_window()
driver.get(url)
for i in range(11):
	ual1 = "https://uathome.uuabc.com/Public/newlogin/index.html#/register"
	username = "1470000" + ''.join(random.sample("12345678901", 4))
	time.sleep(1)
	driver.find_element_by_css_selector("#tips > div.phone > input[type='tel']").clear()
	time.sleep(1)
	driver.find_element_by_css_selector("#tips > div.phone > input[type='tel']").send_keys(username)
	# driver.find_element_by_class_name("phone").send_keys(username)
	time.sleep(1)
	driver.find_element_by_css_selector("#tips > div.pwd > input[type='password']").clear()
	time.sleep(1)
	driver.find_element_by_css_selector("#tips > div.pwd > input[type='password']").send_keys(123456)
	time.sleep(1)
	driver.find_element_by_class_name("enter").click()
	time.sleep(1)
	# if driver.get(url2)
	print(username)
driver.close()
