from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
def login():
    try:
        driver.get("https://text-compare.com/")
        print(driver.title)
       
        WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.ID,"inputText1")))
        driver.find_element(By.ID,"inputText1").send_keys("hi hello welcome to key word action")
        driver.find_element(By.ID, "inputText2")

    except Exception as E:
        print("error occurs in 1st fun : ",E)
def copy_text():
    try:
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        time.sleep(2)
    except Exception as E:
        print("error occurs in 2nd fun : ",E)
def text_past():
    try:
        act = ActionChains(driver)
        act.send_keys(Keys.TAB).perform()
        #driver.find_element(By.ID, "inputText2").send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(3)
    except Exception as E:
        print("error occur in 3rd fun : ",E)
    finally:
        driver.quit()
login()
copy_text()
text_past()
