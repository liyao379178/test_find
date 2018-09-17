from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Shou():

	for r in range(20):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		driver = webdriver.Chrome(executable_path=(r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"),
								  chrome_options=chrome_options)

		url = "https://sit1home.uuabc.com/"
		driver.get(url)
		time.sleep(1)
		cookies = driver.get_cookies()
		time.sleep(1)
		print(f"main: cookies = {cookies}")
		driver.delete_all_cookies()
		print(r)
		driver.quit()


