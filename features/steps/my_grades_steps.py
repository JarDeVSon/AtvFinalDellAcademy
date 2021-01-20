
import os
import time

from behave import use_step_matcher, then, when, given
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys

from features.steps.utils.main_function import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)
use_step_matcher("re")


@given(u'the user accesses the Dell Accessible Learning platform #4.')
def accesses_platform(context):
    context.browser = Firefox()
    context.browser.implicitly_wait(5)
    context.browser.get("https://teste.leadfortaleza.com.br/ead2pcd/")
    login(context.browser, "alunoauditivo26", "abcd1234")


@when(u'the user selects the My Grades on the left menu.')
def my_grades_menu(context):
    time.sleep(5)
    wait = WebDriverWait(context.browser, 20)
    wait.until(EC.element_to_be_clickable((By.ID, "nav-item-4")))
    my_grades_menu = context.browser.find_element_by_id("nav-item-4")
    my_grades_menu.click()
@then(u'the platform returns to the user the grades of his respective courses.')
def my_grades_courses(context):
    wait = WebDriverWait(context.browser, 20)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='buscarCurso']")))
    context.browser.quit()