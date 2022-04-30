[200~from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
try:
    def login():

        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.NAME,"txtPassword").send_keys("admin123")
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(5)

    def my_admin():
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//b[contains(text(),'My Info')]")))
        driver.find_element(By.XPATH,"//b[contains(text(),'My Info')]").click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu_admin_viewAdminModule"]/b')))
        driver.find_element(By.XPATH,'//*[@id="menu_admin_viewAdminModule"]/b').click()
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("manali28")
        driver.find_element(By.NAME,"searchSystemUser[employeeName][empName]").send_keys("Manali Kulkarni")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"searchBtn")))
        driver.find_element(By.ID,"searchBtn").click()
        driver.find_element(By.ID,"ohrmList_chkSelectRecord_38").click()
        time.sleep(5)
    login()
    my_admin()
except Exception as er:
    print("error due to: ",er)
finally:
    driver.quit()
