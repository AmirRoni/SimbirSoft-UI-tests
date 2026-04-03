from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class FormFieldsPage(BasePage):
    URL = "https://practice-automation.com/form-fields/"

    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, "textarea#message")

    MILK_CHECKBOX = (By.XPATH, "//input[@value='Milk']")
    COFFEE_CHECKBOX = (By.XPATH, "//input[@value='Coffee']")
    YELLOW_RADIO = (By.XPATH, "//input[@value='Yellow']")

    AUTOMATION_SELECT = (By.ID, "automation")

    SUBMIT_BUTTON = (By.ID, "submit-btn")

    def open_page(self):
        self.open(self.URL)

    def enter_name(self, name: str):
        self.type(self.NAME_INPUT, name)

    def enter_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)

    def select_milk(self):
        self.click(self.MILK_CHECKBOX)

    def select_coffee(self):
        self.click(self.COFFEE_CHECKBOX)

    def select_yellow(self):
        self.click(self.YELLOW_RADIO)

    def select_automation_yes(self):
        select = Select(self.find(self.AUTOMATION_SELECT))
        select.select_by_value("yes")

    def enter_email(self, email: str):
        self.type(self.EMAIL_INPUT, email)

    def enter_message(self, message: str):
        self.type(self.MESSAGE_TEXTAREA, message)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)
