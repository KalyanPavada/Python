from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from pytest_bdd import scenario,given,when,then
import time
@pytest.fixture(autouse=True)
def basic():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
@scenario('../features/new_check.feature','basic search of keyword')
def home():
    pass
@given('browser page open')
def login():
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    print(driver.title)
@when('user searches for gmail')
def action():
    driver.find_element(By.NAME,"q").send_keys("marayya")
    driver.find_element(By.XPATH,"//*[@id='']").click()
@then('result should appear')
def resu():
    t = driver.find_element(By.NAME,"AmbitionBox").text
    assert t == 'AmbitionBox'
