# -*- coding: utf-8 -*-


from selenium import webdriver
import time


# open browser

chromedriver_path = "C:\Users\user\Downloads\chromedriver"

driver = webdriver.Chrome(chromedriver_path)


# enter website

url = "https://www.leju.com.tw"

driver.get(url)


# search a adress

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


# ----- enter next page -----


# remove sections that I don't need

# 0. anchor: fixed

index = driver.find_element_by_class_name("index")

fixed = index.find_elements_by_xpath("*")[0]

child_of_fixed = fixed.find_elements_by_xpath("*")

# 1. middle part

main = child_of_fixed[1]

container = main.find_element_by_class_name("container")

sections = container.find_elements_by_tag_name("section")

for section in sections:
    if sections.index(section) != 1 and sections.index(section) != 4:
        driver.execute_script("""
            var section = arguments[0];
            section.parentNode.removeChild(section)
            """, section)

# 2. lefthand side

lefthandside = child_of_fixed[0]

driver.execute_script("""
    var lefthandside = arguments[0];
    lefthandside.parentNode.removeChild(lefthandside)
    """, lefthandside)

# 3. righthand side

leaflet_map = child_of_fixed[2]

driver.execute_script("""
    var leaflet_map = arguments[0];
    leaflet_map.parentNode.removeChild(leaflet_map)
    """, leaflet_map)
