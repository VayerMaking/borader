from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import config

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=config.driver_path)

URL = "https://www.etoro.com/login"
def site_login():
	driver.get(URL)
	#TODO
	'''
	Patherns in function find_element_by_xpath are not found.
	'''
	username = driver.find_element_by_name("username")
	username.clear()
	username.send_keys(config.username)

	password = driver.find_element_by_name("password")
	password.clear()
	password.send_keys(config.password)

	driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[1]/et-login/et-login-sts/div/div/div/form/button").click()

site_login()
