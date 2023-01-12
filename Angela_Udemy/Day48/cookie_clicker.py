from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver.exe"

clicker = webdriver.Chrome(executable_path=chrome_driver_path)
clicker.get(url="https://orteil.dashnet.org/cookieclicker/")

# accept_cookies = clicker.find_element(By.CSS_SELECTOR, value='.cc__container--open a')
lang_button = clicker.find_element(By.CSS_SELECTOR, value='div #prompt #langSelect-EN')
# nclick_button = clicker.find_element(By.ID, value='#bigCooker')

# accept_cookies.click()
lang_button.click()
# nclick_button.click()



