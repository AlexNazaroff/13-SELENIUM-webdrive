
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Firefox

driver=webdriver.Chrome()
#wait = WebDriverWait(driver, 20)

#driver.implicitly_wait(20) # seconds

#driver.get("http://somedomain/url_that_delays_loading")
#myDynamicElement = driver.find_element_by_id("myDynamicElement")

#driver.get('http://www.python.org')


driver.get('http://board.orsk.ru/')
driver.find_element_by_id("1").click() # Клик по ссылке

driver.find_element_by_link_text("Услуги").click()
driver.find_element_by_link_text("Грузоперевозки").click()

driver.find_element_by_id("account-popover").text # Получаем текст

