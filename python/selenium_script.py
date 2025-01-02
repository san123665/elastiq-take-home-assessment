from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = "path_to_chrome"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
try:
    driver.get("https:www.google.com")
    driver.maxmize_window()
    time.sleep(2)
    search_bar = driver.find_elemt(By.ID,"userinput")
    search_query = "checkbox demo"
    search_bar.send_keys(search_query)
    time.sleep(1)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.CLASS_NAME,"class_name")
    if results:
        print(f"Search query for {search_query}")
        for index, result in enumerate(results,start=1):
            print(f"{index} {result.txt}")
    else:
        print("no records found")
finally:
    driver.quit()