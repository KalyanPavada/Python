from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from pytest_bdd import scenario,given,when,then,parsers
import time

@scenario('../features/check_orangehrm.feature','basic search of keyword')
def test_home1():
    pass
@given('browser page open')
def open_page(basic):
    global driver
    driver = basic
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
    print(driver.title)
@when(parsers.parse('user searches for {username},{password}'))
def action(username,password):
    driver.find_element(By.ID,"txtUsername").send_keys(username)
    driver.find_element(By.ID,"txtPassword").send_keys(password)
    time.sleep(1)
@when("user login into the page")
def login():
    driver.find_element(By.ID,"btnLogin").send_keys(Keys.ENTER)

@then('user successfully login to the dashboard page')
def resu():
    t = driver.find_element(By.XPATH,"//b[contains(text(),'Dashboard')]").text
    assert t == 'Dashboard'
