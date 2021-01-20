

def login(browser, username, password):

    login_field = browser.find_element_by_id("login")
    login_field.send_keys(username)
    password_field = browser.find_element_by_id("password")
    password_field.send_keys(password)
    button_enter = browser.find_element_by_id("login-btn")
    button_enter.click()