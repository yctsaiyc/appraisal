# -*- coding: utf-8 -*-
# if not type the first line, Chinese can not be used


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# open browser

chromedriver_path = "C:\Users\user\Downloads\chromedriver"

driver = webdriver.Chrome(chromedriver_path)


# enter website

url = "https://www.leju.com.tw"

driver.get(url)


# remove the title (just for fun)

element = driver.find_element_by_tag_name("h2")

driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)


# search an adress

# step 1. click button so that selenium can interact with the list

button_of_drop_down_list_of_city = driver.find_element_by_class_name("banner-form__new-search__select-block__city-option")

button_of_drop_down_list_of_city.click()

# step 2. choose city (the first one is Taipei)

city = driver.find_element_by_class_name("list-available-item")

city.click()

# step 3. click search bar

search_bar = driver.find_element_by_class_name("banner-form__new-search__select-block__search-object")

search_bar.click()

# step 4. type in input bar

input_bar = driver.find_element_by_class_name("select-option__input")

input_bar.send_keys(u"信義聯勤")

# step 5. click option

option = driver.find_element_by_class_name("select-option")

# sleep (if not sleep, selenium would click before option show up)

time.sleep(1)

option.click()
