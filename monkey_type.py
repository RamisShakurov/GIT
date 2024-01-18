from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementNotInteractableException

url = "https://monkeytype.com/"

with webdriver.Chrome() as driver:
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="cookiePopup"]/div[2]/div[2]/button[1]').click()
    text = driver.find_element(By.ID, 'words')
    try:
        while text.find_element(By.CLASS_NAME, 'active'):
            send_key = text.find_element(By.CLASS_NAME, 'active')
            btn = driver.find_element(By.ID, 'wordsInput')
            btn.send_keys(send_key.text)
            btn.send_keys(Keys.SPACE)
    except ElementNotInteractableException:
        print("finish")

    sleep(10)


