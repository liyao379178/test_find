#coding=utf-8
from selenium import webdriver
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()


def driver_init():
	driver.get("https://www.uuabc.com")
	driver.maximize_window()
	driver.implicitly_wait(30)


def get_element():
	element = driver.find_element_by_id(id)
	return element

#radom
def get_range_user():
	user_info = '147'+''.join(random.sample('1234567890',8))
	return user_info

#验证码截取
def get_code_image(file_name):
	driver.save_screenshot(file_name)
	code_element = driver.find_element_by_id("")
	left = code_element.location['x']
	top = code_element.location['y']
	right = code_element.size['width']+left
	height = code_element.size['height']+top
	im = Image.open(file_name)
	img = im.crop(left,top,right,height)
	img.save(file_name)

#付费接口识别验证码
def code_online(file_name):
	r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "3f85994cc5a073165cbadf7d58618dad")
	r.addBodyPara("typeId", "34")
	r.addBodyPara("needMorePrecise", "0")
	r.addFilePara("image", file_name)  # 文件上传时设置
	res = r.post()
	test = res.json()["showapi_res_body"]["Result"]
	return test

def run_main():
	user_email = get_range_user()
	driver_init()
	get_element().send_keys(user_email)
