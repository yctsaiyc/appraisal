# -*- coding: utf-8 -*-


from selenium import webdriver
import time


def leju():

    # open browser
    chromedriver_path = "C:\Users\user\Downloads\chromedriver"
    driver = webdriver.Chrome(chromedriver_path)

    # maximize window
    driver.maximize_window()

    # enter website
    url = "https://www.leju.com.tw"
    driver.get(url)

    return driver


def search_in_Taipei(driver, adress=u"信義聯勤"):

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
    input_bar.send_keys(adress)

    # -- wait for loading
    time.sleep(1)
    
    # step 5. click option
    option = driver.find_element_by_class_name("select-option")
    option.click()

    # -- wait for loading
    time.sleep(1)


def rm_useless(driver):

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
   
    # 4. useless info in basic-info
    infos = driver.find_element_by_class_name("basic-info").find_elements_by_xpath("*")
    for info in infos[1:]:
        driver.execute_script("""
            var info = arguments[0];
            info.parentNode.removeChild(info)
            """, info)
        
    return container

def screenshot(element, name="screenshot.png"):
    driver.execute_script("arguments[0].style.zoom='0.7'", element)
    element.screenshot(name)


# ------------------------------------------------------------------


driver = leju()

while True:
    i = 1
    adress = raw_input("Enter an adress or neighborhood: ")
    search_in_Taipei(driver, adress=adress)
    element = rm_useless(driver)
    name = "case" + str(i) + ".png"
    screenshot(element, name=name)
    i += 1
