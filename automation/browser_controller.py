# automation/browser_controller.py

from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserController:
    def __init__(self, headless: bool = False):
        self.driver = Driver(uc=True, headless=headless)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, by: By, value: str, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, by: By, value: str):
        element = self.find(by, value)
        element.click()

    def type(self, by: By, value: str, text: str):
        element = self.find(by, value)
        element.clear()
        element.send_keys(text)

    def screenshot(self, path: str):
        self.driver.save_screenshot(path)

    def close(self):
        self.driver.quit()