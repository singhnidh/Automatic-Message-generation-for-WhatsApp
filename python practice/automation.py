from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

contact = "Di WhatsApp"
text = "Hey, this message was sent using Selenium"

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

inp_xpath_search = "//input[@title='Search or start new chat']"

# Increase the timeout duration to 60 seconds (instead of 50)
time.sleep(50)
input_box_search = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, inp_xpath_search)))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='" + contact + "']")
selected_contact.click()

inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)

time.sleep(2)
driver.quit()
