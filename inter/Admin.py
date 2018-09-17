from PIL import Image
import time
from selenium import webdriver
import random


class Uadmin(object):

	driver = webdriver.Chrome()
	driver.maximize_window()
	url = 'http://admin.uuabc.com/index.php?m=Home&c=Login&a=index'
	driver.get(url)
	driver.implicitly_wait(30)

	driver.find_elements_by_class_name("form-control")[0].send_keys("liyao")
	time.sleep(1)
	driver.find_elements_by_class_name("form-control")[1].send_keys("123456")
	time.sleep(1)
	image = driver.find_element_by_class_name("verify-img")
	driver.save_screenshot(image)
	driver.find_element_by_css_selector("body > div.container > form > div.login-wrap > button").click()
	find = driver.find_element_by_link_text("欢迎进入后台管理系统")

	okey = ''.join(random.sample('abcdefghijklmnopkrstuvwxyz',1))
	driver.find_elements_by_class_name("form-control")[2].send_keys(okey)


