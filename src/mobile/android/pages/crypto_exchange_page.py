from src.mobile.android.pages.base_page import BasePage
from src.mobile.android.locators.crypto_exchange_locators import CryptoExchangeLocators
from src.utils.logger import setup_logger
import time

logger = setup_logger(__name__)

class CryptoExchangePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def select_from_currency(self, currency="ARS"):
        logger.info(f"Selecting from currency: {currency}")
        self.click(CryptoExchangeLocators.FROM_CURRENCY_DROPDOWN)
        
        if currency.upper() == "ARS":
            self.click(CryptoExchangeLocators.ARS_OPTION)
        elif currency.upper() == "USDT":
            self.click(CryptoExchangeLocators.USDT_OPTION)
    
    def select_to_currency(self, currency="USDT"):
        logger.info(f"Selecting to currency: {currency}")
        self.click(CryptoExchangeLocators.TO_CURRENCY_DROPDOWN)
        
        if currency.upper() == "ARS":
            self.click(CryptoExchangeLocators.ARS_OPTION)
        elif currency.upper() == "USDT":
            self.click(CryptoExchangeLocators.USDT_OPTION)
    
    def enter_amount(self, amount):
        logger.info(f"Entering amount: {amount}")
        self.send_keys(CryptoExchangeLocators.AMOUNT_INPUT, str(amount))
    
    def calculate_exchange(self):
        logger.info("Calculating exchange")
        self.click(CryptoExchangeLocators.CALCULATE_BUTTON)
        time.sleep(2)  # Wait for calculation
    
    def get_exchange_rate(self):
        try:
            rate_text = self.get_text(CryptoExchangeLocators.EXCHANGE_RATE)
            return rate_text
        except:
            return "Exchange rate not found"
    
    def get_estimated_amount(self):
        try:
            estimated_text = self.get_text(CryptoExchangeLocators.ESTIMATED_AMOUNT)
            return estimated_text
        except:
            return "Estimated amount not found"
    
    def execute_exchange(self):
        logger.info("Executing exchange")
        self.click(CryptoExchangeLocators.EXCHANGE_BUTTON)
        
        # Confirm the exchange
        if self.is_element_visible(CryptoExchangeLocators.CONFIRM_BUTTON):
            self.click(CryptoExchangeLocators.CONFIRM_BUTTON)
    
    def is_exchange_successful(self):
        try:
            return self.is_element_visible(CryptoExchangeLocators.SUCCESS_MESSAGE)
        except:
            return False
    
    def perform_crypto_exchange(self, from_currency, to_currency, amount):
        self.select_from_currency(from_currency)
        self.select_to_currency(to_currency)
        self.enter_amount(amount)
        self.calculate_exchange()
        
        rate = self.get_exchange_rate()
        estimated = self.get_estimated_amount()
        
        logger.info(f"Exchange rate: {rate}")
        logger.info(f"Estimated amount: {estimated}")
        
        self.execute_exchange()
        return self.is_exchange_successful()