from src.mobile.android.pages.base_page import BasePage
from src.mobile.android.locators.login_locators import LoginLocators
from src.utils.config import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def login(self, email=None, password=None):
        email = email or Config.VITA_USER
        password = password or Config.VITA_PASSWORD
        
        logger.info(f"Logging in with email: {email}")
        
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)
        
        # Handle skip button if present
        if self.is_element_visible(LoginLocators.SKIP_BUTTON):
            self.click(LoginLocators.SKIP_BUTTON)
        
        return self.is_login_successful()
    
    def is_login_successful(self):
        try:
            return self.is_element_visible(LoginLocators.WELCOME_MESSAGE)
        except:
            return False