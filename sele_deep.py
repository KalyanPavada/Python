from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
def login():
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")
        print(driver.title)

        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"btnLogin")))
        driver.find_element(By.ID,"btnLogin").send_keys(Keys.ENTER)
    except Exception as E:
        print("error due to 1st function : ",E)
def my_leave():
    try:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//tbody/tr[1]/td[5]/div[1]/a[1]/img[1]")))
        driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/div[1]/a[1]/img[1]").click()

        driver.find_element(By.ID,"calFromDate").click()
        driver.find_element(By.XPATH,"//body/div[@id='ui-datepicker-div']/div[1]/div[1]/select[1]").click()
        time.sleep(2.5)
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='ui-datepicker-div']/div[1]/div[1]/select[1]")))
        driver.find_element(By.XPATH,"//body/div[@id='ui-datepicker-div']/div[1]/div[1]/select[1]").click()
        # driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[1]/a').click()
        driver.find_element(By.XPATH,"//tbody/tr[4]/td[5]/a[1]").click()
        driver.find_element(By.XPATH,"//input[@id='calToDate']").click()
        driver.find_element(By.XPATH,"//tbody/tr[4]/td[7]/a[1]").click()
        time.sleep(3)

    except Exception as E:
        print("Error occurs to 2ND function: ",E)
def scroll():
    try:
        driver.find_element(By.XPATH,"//b[contains(text(),'Recruitment')]").click()
        scroll = driver.find_element(By.XPATH,"//a[contains(text(),'Butler')]")
        ActionChains(driver).move_to_element(scroll).perform()
        time.sleep(2)
    except Exception as E:
        print("Error occurs to 3rd fun : ",E)
def new_tab_ifram():
    try:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://contests.heymath.com/RI22")
        print(driver.title)
        in_frame = driver.find_element(By.TAG_NAME,"iframe")
        driver.switch_to.frame(in_frame)
        driver.find_element(By.ID,"loginBtn").click()
        driver.switch_to.parent_frame()
        driver.find_element(By.NAME,"plp_userinput").send_keys("kalyan")
        driver.find_element(By.NAME,"password").send_keys("451255")
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/i[1] ").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    except Exception as E:
        print("Error occurs 4th fun : ",E)
    finally:
        driver.quit()
login()
my_leave()
scroll()
new_tab_ifram()





