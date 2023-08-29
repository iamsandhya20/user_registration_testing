import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")
driver = webdriver.Edge()

def before_scenario(context, scenario):
    context.driver = webdriver.Edge()
    context.driver.get("https://google.com")
    time.sleep(3)

def after_scenario(context, scenario):
    context.driver.quit()

@given("the user is on the registration page")
def step_impl(context):
    driver.get("https://cts-saepn.formstack.com/forms/registration_from")
    time.sleep(3)

@when('they enter "(?P<username>.+)" and "(?P<email>.+)"')
def step_impl(context, username, email):
    driver.find_element(By.ID, "field150045447-first").send_keys("Sandhya")
    driver.find_element(By.ID, "field150045451").send_keys("sandhyamax20@gmail.com")
    time.sleep(5)

@when('they set the password to "(?P<password>.+)"')
def step_impl(context, password):
    driver.find_element(By.ID, "field150045473").send_keys("sandhya20")
    time.sleep(5)

@when("they confirm the password")
def step_impl(context):
    password = driver.find_element(By.ID, "field150045473").get_attribute("value")
    driver.find_element(By.ID, "field150045474").send_keys("sandhya20")
    time.sleep(3)

@then("the registration should be successful")
def step_impl(context):
    driver.find_element(By.ID, "fsSubmitButton5415346")
