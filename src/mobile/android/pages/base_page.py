from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
    
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        element = self.find_element(locator)
        element.click()
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def wait_for_element_to_disappear(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
    
    def take_screenshot(self, name):
        screenshot_path = f"./reports/screenshots/{name}.png"
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path