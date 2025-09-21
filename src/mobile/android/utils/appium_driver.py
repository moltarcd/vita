from appium import webdriver
from appium.options.android import UiAutomator2Options
from src.utils.config import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class AppiumDriver:
    _instance = None
    
    @classmethod
    def get_driver(cls):
        if cls._instance is None:
            cls._instance = cls._initialize_driver()
        return cls._instance
    
    @classmethod
    def _initialize_driver(cls):
        try:
            options = UiAutomator2Options()
            options.platform_name = Config.PLATFORM_NAME
            options.device_name = Config.DEVICE_NAME
            options.automation_name = Config.AUTOMATION_NAME
            options.app = Config.APP_PATH
            options.app_package = Config.APP_PACKAGE
            options.app_activity = Config.APP_ACTIVITY
            options.new_command_timeout = 300
            
            # Additional capabilities
            options.set_capability('autoGrantPermissions', True)
            options.set_capability('autoAcceptAlerts', True)
            options.set_capability('unicodeKeyboard', True)
            options.set_capability('resetKeyboard', True)
            
            logger.info(f"Connecting to Appium server: {Config.APPIUM_SERVER_URL}")
            driver = webdriver.Remote(
                Config.APPIUM_SERVER_URL,
                options=options
            )
            
            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            logger.info("Appium driver initialized successfully")
            return driver
            
        except Exception as e:
            logger.error(f"Failed to initialize Appium driver: {e}")
            raise
    
    @classmethod
    def quit_driver(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None
            logger.info("Appium driver quit successfully")