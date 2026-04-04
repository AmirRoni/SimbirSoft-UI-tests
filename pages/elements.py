from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class PageElement:
    def __init__(self, locator):
        self.locator = locator

    def find(self, page, timeout: int = 10):
        return WebDriverWait(page.driver, timeout).until(
            EC.presence_of_element_located(self.locator)
        )


class InputElement(PageElement):
    def set(self, page, text: str, timeout: int = 10):
        element = WebDriverWait(page.driver, timeout).until(
            EC.visibility_of_element_located(self.locator)
        )
        page.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element.clear()
        element.send_keys(text)


class ButtonElement(PageElement):
    def click(self, page, timeout: int = 10):
        element = WebDriverWait(page.driver, timeout).until(
            EC.element_to_be_clickable(self.locator)
        )
        page.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            page.driver.execute_script("arguments[0].click();", element)
