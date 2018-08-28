from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import pymysql
import re


class New():
	driver = webdriver.Chrome()
	# driver.maximize_window()
	f = open("C:\\Users\\user\\PycharmProjects\\test_find\\账号.txt","w")
	for i in range(1):	# 修改range里的值，可以注册对应的账号

		user = "1470000" + ''.join(random.sample("1234567890",4))  # 随机user手机号
		url = "https://uathome.uuabc.com/Public/newlogin/index.html#/register"
		driver.get(url)
		time.sleep(1)
		driver.find_element_by_id("phone").clear()
		driver.find_element_by_id("phone").send_keys(user)  # 传入user手机号
		time.sleep(1)
		driver.find_element_by_class_name("badge").click()

		time.sleep(2)
		driver.find_element_by_id("code").clear()
		"""
		数据库查询user对应的短信
		"""
		conn = pymysql.connect(host="uathome.uuabc.com",
							   user="wufenfen",
							   password="wufenfen",
							   db="newuuabc",
							   port=3306,
							   charset="utf8"
							   )

		"""
		接口查询用户短信
		"""
		cur = conn.cursor()
		cur.execute("SELECT  sms_send.content FROM sms_send WHERE phone='" + user + "'")
		re_dock = cur.fetchone()
		cur.close()

		r = re.findall('\d{6}', str(re_dock))  # 正则获取短信验证码
		driver.find_element_by_id("code").clear()
		time.sleep(1)
		driver.find_element_by_id("code").send_keys(r)
		time.sleep(1)
		driver.find_element_by_id("name").clear()
		name = "测试" + ''.join(random.sample("你真的很逗比", 2))  # 随机用户name
		driver.find_element_by_id("name").send_keys(name)
		time.sleep(1)
		driver.find_element_by_id("pwd").clear()
		driver.find_element_by_id("pwd").send_keys(123456)
		time.sleep(1)
		driver.find_element_by_css_selector("#app > div > div.wrapper > div > div.main > a").click()
		time.sleep(2)
		next_one = driver.find_element_by_class_name("skipBtn")

		# 点击下一步判断，如注册失败后，截图存入image
		if next_one== None:
			driver.save_screenshot("C:\\Users\\user\\PycharmProjects\\test_find\\image\\" + user + ".png")
			driver.close()
		else:
			f.write(user + "\n")
		time.sleep(1)

		cookies = driver.get_cookies()
		time.sleep(1)
		# print(f"main: cookies = {cookies}")
		driver.delete_all_cookies()
		time.sleep(2)

	f.write("\n"+"注册完成的账号，每次执行后上一次数据会被替换掉")
	f.close()
	driver.close()

