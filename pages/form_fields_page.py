from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class FormFieldsPage(BasePage):
    URL = "https://practice-automation.com/form-fields/"

    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, "textarea#message")

    AUTOMATION_SELECT = (By.ID, "automation")
    SUBMIT_BUTTON = (By.ID, "submit-btn")

    AUTOMATION_TOOLS_ITEMS = (
        By.XPATH,
        "//*[normalize-space()='Automation tools']/following-sibling::ul[1]/li"
    )

    def open_page(self):
        self.open(self.URL)

    def enter_name(self, name: str):
        self.type(self.NAME_INPUT, name)

    def enter_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)

    def select_drinks(self, drinks: list[str]):
        for drink in drinks:
            locator = (By.XPATH, f"//input[@value='{drink}']")
            self.click(locator)

    def select_color(self, color_name: str):
        locator = (By.XPATH, f"//input[@value='{color_name}']")
        self.click(locator)

    def select_automation_option(self, value: str):
        select = Select(self.find(self.AUTOMATION_SELECT))
        select.select_by_value(value)

    def enter_email(self, email: str):
        self.type(self.EMAIL_INPUT, email)

    def enter_message(self, message: str):
        self.type(self.MESSAGE_TEXTAREA, message)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)

    def get_alert_text_and_accept(self, timeout=10) -> str:
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    def get_automation_tools(self) -> list[str]:
        elements = self.driver.find_elements(*self.AUTOMATION_TOOLS_ITEMS)
        texts = []

        for element in elements:
            text = element.text.strip()
            if text:
                texts.append(text)

        return texts

    def build_message_from_automation_tools(self) -> str:
        tools = self.get_automation_tools()
        tools_count = len(tools)
        longest_tool = max(tools, key=len)
        return f"{tools_count} {longest_tool}"
