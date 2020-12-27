# code for home button

# code for portfolio button

# code for services button

# code for Contact Us button

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")


home_text = driver.find_element_by_xpath('//*[@id="rec91259711"]//div[4]/a')
assert home_text.text == "Home"

portfolio_text = driver.find_element_by_xpath('//*[@id="rec91259711"]//div[5]/a')
assert portfolio_text.text == "Portfolio"

services_text = driver.find_element_by_xpath('//*[@id="rec91259711"]//div[6]/a')
assert services_text.text == "Services"

contact_us_text = driver.find_element_by_xpath("(//a[text()='Contact Us'])[1]")
assert contact_us_text.text == "Contact Us"

driver.quit()
