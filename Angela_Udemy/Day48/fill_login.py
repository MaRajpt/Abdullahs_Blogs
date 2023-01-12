from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

f_name= driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value='email')
button = driver.find_element(By.CLASS_NAME, value='btn-block')


f_name.send_keys("Tobi")
l_name.send_keys('Kazachi')
email.send_keys('yoloswag@mail.com')
button.send_keys(Keys.ENTER)

