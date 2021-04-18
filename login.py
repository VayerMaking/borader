from selenium import webdriver
import config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=config.driver_path)

URL = "https://www.etoro.com/login"
def site_login():

	username = "Borader"
	password = "Reqreqreq03"

	driver.get(URL)
	#TODO
	'''
	Patherns in function find_element_by_xpath are not found. Sad. Searched in stack Overflow but didn't found anything

	Etoro is bloccking remote controlled browsers
	'''
	username = driver.find_element_by_name("username")
	username.clear()
	username.send_keys(config.username)

	password = driver.find_element_by_name("password")
	password.clear()
	password.send_keys(config.password)

	driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[1]/et-login/et-login-sts/div/div/div/form/button").click()

site_login()
