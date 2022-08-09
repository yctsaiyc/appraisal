from selenium import webdriver


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


# search a adress

# step 1. click button so that selenium can interact with the list

button_of_drop_down_list_of_city = driver.find_element_by_class_name("banner-form__new-search__select-block__city-option")

button_of_drop_down_list_of_city.click()

# step 2. choose city (the first one is Taipei)

city = driver.find_element_by_class_name("list-available-item")

city.click()




