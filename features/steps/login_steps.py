import os
import sys

from behave import given, when, then, use_step_matcher
from nose.tools import assert_equal
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)
use_step_matcher("re")

@given(u'the user accesses the Dell Accessible Learning platform.')
def accesses_platform(context):
    context.browser = Firefox()
    context.browser.get("https://teste.leadfortaleza.com.br/ead2pcd/")

@when(u'the user authenticates with valid credentials.')
def authenticates(context):
    login_field = context.browser.find_element_by_id("login")
    login_field.send_keys("alunoauditivo26")
    password_field = context.browser.find_element_by_id("password")
    password_field.send_keys("abcd1234")
    button_enter = context.browser.find_element_by_id("login-btn")
    button_enter.click()
@then(u'the platform returns the home page to the user.')
def home_page(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "nav-item-0")))
    context.browser.quit()