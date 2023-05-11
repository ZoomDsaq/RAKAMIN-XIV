from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

##Feature Login

driver= webdriver.Chrome()
#Scenario Valid Test
@given('Im at the sign-in page')
def jubeliopage(context):
    driver.delete_all_cookies()
    driver.get("https://app.jubelio.com/login")
    time.sleep(2)

@when('I enter valid email and password')
def credentials_input(context):
    username_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[1]/div/input')
    username_input.send_keys("qa.rakamin.jubelio@gmail.com")
    password_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[2]/div/input')
    password_input.send_keys("Jubelio123!")

@when('I click the login button')
def login(context):
    login_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/button')
    login_button.click()
    time.sleep(3)

@then('I should be redirected to my jubelio home page')
def step_impl(context):
    assert "home" in driver.current_url 
    time.sleep(2)

#Scenario Invalid Test
@given('Im at the login page')
def jubeliopage(context):
    driver.delete_all_cookies()
    driver.get("https://app.jubelio.com/login")
    time.sleep(2)

@when('I leave the login credentials empty and click on the login button')
def credentials_input(context):
    username_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[1]/div/input')
    username_input.send_keys("")
    password_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[2]/div/input')
    password_input.send_keys("Jubelio123!")
    login_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/button')
    login_button.click()
    time.sleep(3)

@then('I should not be logged in and should receive an error message')
def step_impl(context):
    assert  driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[1]/div/span')
    driver.quit()

