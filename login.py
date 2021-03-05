from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")
driver = webdriver.Firefox(options=options, executable_path=r'/home/petar/Desktop/geckodriver')

URL = "https://www.etoro.com/login"
def site_login():
	username_id = "username"
	username = "petar.dmnv03@gmail.com"
	password_id = "password"
	password = "reqreqreq03"
	sign_btn_id = "login-sts-btn-sign-in"

	driver.get(URL)
	#TODO
	'''
	Patherns in function find_element_by_xpath are not found.
	'''
	driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[1]/et-login/et-login-sts/div/div/div/form/div[1]").send_keys(username)
	driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[1]/et-login/et-login-sts/div/div/div/form/div[2]").send_keys(password)
	driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[1]/et-login/et-login-sts/div/div/div/form/button").click()

site_login()