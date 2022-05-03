[200~from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
try:
    def login():
        driver.get("https://opensource-demo.orangehrmlive.com/")
        print(driver.title)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(2)
    def new_tab():
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://search.yahoo.com/search?fr=mcafee&type=E211US714G91671&p=gmail")
        print(driver.title)
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//a[contains(text(),'Contacts')]")))
        my_text = driver.find_element(By.XPATH,"//a[contains(text(),'Contacts')]").text
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(By.ID,"txtUsername").clear()
        driver.find_element(By.ID,"txtUsername").send_keys(my_text)
        driver.find_element(By.ID,"btnLogin").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.close()
    login()
    new_tab()
except Exception as e:
    print(e)
finally:
    driver.quit()
