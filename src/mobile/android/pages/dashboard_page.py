from src.mobile.android.pages.base_page import BasePage
from src.mobile.android.locators.dashboard_locators import DashboardLocators
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_crypto(self):
        logger.info("Navigating to Crypto tab")
        self.click(DashboardLocators.CRYPTO_TAB)
    
    def get_balance(self):
        try:
            balance_text = self.get_text(DashboardLocators.BALANCE_TEXT)
            return balance_text
        except:
            return "Balance not found"