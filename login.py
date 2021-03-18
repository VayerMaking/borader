from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Firefox(options=options, executable_path=r'/home/petar/Desktop/geckodriver')

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
	'''driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[1]/et-login/et-login-sts/div/div/div/form/div[1]").send_keys(username)
	driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[1]/et-login/et-login-sts/div/div/div/form/div[2]").send_keys(password)
	driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[1]/et-login/et-login-sts/div/div/div/form/button").click()'''

	#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.w-login-main-form-input.ng-valid-email.ng-invalid-required.ng-valid-pattern"))).send_keys(username)
	
	driver.find_element_by_css_selector("input.w-login-main-form-input.ng-valid-email.ng-invalid-required.ng-valid-pattern").send_keys(password)
	driver.find_element_by_css_selector("input.w-login-main-form-input[type='password']").send_keys(password)
	driver.find_element_by_css_selector("button.e-btn-big.wide.dark.pointer[automation-id='login-sts-btn-sign-in']").click()

def buy_sth():
	pass
'''
If headless option is true We think that if will log in to site
'''

site_login()