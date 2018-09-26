import re
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
val=["12","abcg345677"]
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("https://vanilla-masker.github.io/vanilla-masker/demo.html")
search_field = driver.find_element_by_id("zeroCents")
for i in val:
	search_field.clear()
	search_field.send_keys(i)
	print search_field.get_attribute('value')
i="shilpa"
for char in i:
	print char
	