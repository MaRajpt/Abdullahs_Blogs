from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")         # there are 2 a tags but i goes till frist a tag (not second)

# article_count.click()

links_ = driver.find_element(by=By.LINK_TEXT, value="Nominate an article")
# links_.click()

search = driver.find_element(by=By.NAME, value='search')  # 'search' is the name of input tag search
search.send_keys("Python")        # keys of keyboard
search.send_keys(Keys.ENTER)    # enter key on keyboard















