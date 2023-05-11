from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
actions = ActionChains(driver)

##Feature manage stocks
#Scenario Adding stocks
@given('Im at the home page')
def jubeliopage(context):
    driver.delete_all_cookies()
    driver.get("https://app.jubelio.com/login")
    time.sleep(2)
    username_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[1]/div/input')
    username_input.send_keys("qa.rakamin.jubelio@gmail.com")
    password_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[2]/div/input')
    password_input.send_keys("Jubelio123!")
    login_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/button')
    login_button.click()
    time.sleep(5)

@when('Im at the homepage, I click the Akunting menu and the Penyesuaian button')
def akuntingmenu(context):
    akunting_button = driver.find_element(By.XPATH,'//*[@id="wrapper"]/nav/div/div/ul/li[6]/a')
    akunting_button.click()
    time.sleep(1)
    persediaan_button = driver.find_element(By.XPATH,'//*[@id="wrapper"]/nav/div/div/ul/li[6]/ul/li[1]/a')
    persediaan_button.click()
    time.sleep(1)
    penyesuaian_button = driver.find_element(By.XPATH,'//*[@id="wrapper"]/nav/div/div/ul/li[6]/ul/li[1]/ul/li[1]/a')
    penyesuaian_button.click()
    time.sleep(3)    

@when('I click the tambah baru button to increase my goods stocks')
def increasing_stocks(context):
    tmbhbru_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/button')
    tmbhbru_button.click()
    time.sleep(1)
    qntity_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li[1]/a')
    qntity_button.click()
    time.sleep(1)
    chsgds_list = driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/span/div')
    actions.double_click(chsgds_list).perform()
    time.sleep(1)
    chsgds = driver.find_element(By.XPATH,'/html[1]/body[1]/div[6]/div[1]/div[1]/div[2]/div[2]/div[17]')
    chsgds.click()
    time.sleep(2)
    qtitychngclk = driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div')
    actions.double_click(qtitychngclk).perform()
    time.sleep(0.5)
    qtitychng = driver.find_element(By.XPATH,'/html/body/div[6]/div/input')
    qtitychng.send_keys('2')
    qtitychng.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    simpan_button = driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[3]/span[1]')
    simpan_button.click()
    time.sleep(2)

@then('Successfully added the number of items')
def Success_adding_stocks(context):
    assert driver.find_element(By.XPATH,('//*[@id="root"]/div/div[1]'))
    time.sleep(2) 