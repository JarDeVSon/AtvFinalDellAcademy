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

@given(u'the user accesses the Dell Accessible Learning platform #3.')
def accesses_platform(context):
    context.browser = Firefox()
    context.browser.implicitly_wait(5)
    context.browser.get("https://teste.leadfortaleza.com.br/ead2pcd/")
    login(context.browser, "alunoauditivo26", "abcd1234")


@when(u'the user selects the My Agenda on the left menu.')
def my_agenda_menu(context):
    #time.sleep(5)
    wait = WebDriverWait(context.browser, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-item-2']")))
    my_agenda_menu = context.browser.find_element_by_xpath("//*[@id='nav-item-2']")
    my_agenda_menu.click()
@then(u'the platform returns to the user the date of his classes respective courses.')
def my_agenda_information(context):
    wait = WebDriverWait(context.browser, 20)
    wait.until(EC.presence_of_element_located((By.ID, "scheduleCalendar")))
    context.browser.quit()