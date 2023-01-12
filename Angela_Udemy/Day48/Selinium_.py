from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url ="https://www.python.org/")

get_events = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget .menu li a')
get_dates = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget .menu time')

events = []
dates = []

for event in get_events:
    events.append(event.text)

for date in get_dates:
    dates.append(date.text)

data_dict = dict(zip(events, dates))





driver.close()

# driver.quit() closes entire browser whereas driver.close() closes the tab

'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]'