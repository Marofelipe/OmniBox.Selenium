from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://letterboxd.com/")

driver.implicitly_wait(10)

driver.close()