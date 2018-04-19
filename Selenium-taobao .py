from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


broswer= _webdriver.Chrome()
wait=WebDriverWait(broswer, 10)
def search():
	broswer.get('https://www.taobao.com')
	 input = wait.until(
        EC.presence_of_element_located((By.CSS_SLECTOR, "#q"))
    )
	 submit =wait.until() 