from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.elements import InputElement, ButtonElement


class FormFieldsPage(BasePage):
    URL = "https://practice-automation.com/form-fields/"

    name_input = InputElement((By.ID, "name-input"))
    password_input = InputElement((By.XPATH, "//input[@type='password']"))
    email_input = InputElement((By.ID, "email"))
    message_textarea = InputElement((By.CSS_SELECTOR, "textarea#message"))
    submit_button = ButtonElement((By.ID, "submit-btn"))

    AUTOMATION_SELECT = (By.ID, "automation")
    AUTOMATION_TOOLS_ITEMS = (
        By.XPATH,
        "//*[normalize-space()='Automation tools']/following-sibling::ul[1]/li"
    )

    def open_page(self):
        self.open(self.URL)
        return self

    def enter_name(self, name: str):
        self.name_input.set(self, name)
        return self

    def enter_password(self, password: str):
        self.password_input.set(self, password)
        return self

    def select_drinks(self, drinks: list[str]):
        for drink in drinks:
            locator = (By.XPATH, f"//input[@value='{drink}']")
            self.click(locator)
        return self

    def select_color(self, color_name: str):
        locator = (By.XPATH, f"//input[@value='{color_name}']")
        self.click(locator)
        return self

    def select_automation_option(self, value: str):
        select = Select(self.find(self.AUTOMATION_SELECT))
        select.select_by_value(value)
        return self

    def enter_email(self, email: str):
        self.email_input.set(self, email)
        return self

    def enter_message(self, message: str):
        self.message_textarea.set(self, message)
        return self

    def submit_form(self):
        self.submit_button.click(self)
        return self

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
