from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOCATOR_LOGIN_INPUT = (By.ID, "email")
    LOCATOR_PASSWORD_INPUT = (By.ID, "password")
    LOCATOR_INPUT_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    LOCATOR_REGISTRATION_BTN = (By.XPATH, '//*[@id="app"]/div/div/div/div/form/div[3]/button')
    LOCATOR_ORGANIZATION_NAME = (By.CLASS_NAME, "user__menu-organization-name")
    LOCATOR_ALERT_INCORRECT_DATA = (By.CLASS_NAME, "el-message el-message--error")