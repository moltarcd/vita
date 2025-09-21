import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class Config:
    """Configuration class for API and Mobile tests"""

    # -----------------------------
    # API Configuration
    # -----------------------------
    PETSTORE_BASE_URL = os.getenv('PETSTORE_BASE_URL', 'https://petstore.swagger.io/v2')

    # -----------------------------
    # Mobile Configuration (Appium)
    # -----------------------------
    APPIUM_SERVER_URL = os.getenv('APPIUM_SERVER_URL', 'http://localhost:4723/wd/hub')
    APP_PATH = os.getenv('APP_PATH', '')
    PLATFORM_NAME = os.getenv('PLATFORM_NAME', 'Android')
    DEVICE_NAME = os.getenv('DEVICE_NAME', 'emulator-5554')
    AUTOMATION_NAME = os.getenv('AUTOMATION_NAME', 'UiAutomator2')
    PLATFORM_VERSION = os.getenv('PLATFORM_VERSION', '11.0')
    APP_PACKAGE = os.getenv('APP_PACKAGE', 'io.vitawallet.wallet')
    APP_ACTIVITY = os.getenv('APP_ACTIVITY', 'io.vitawallet.wallet.MainActivity')

    # -----------------------------
    # Vita Wallet credentials
    # -----------------------------
    VITA_USER = os.getenv('VITA_USER', '')
    VITA_PASSWORD = os.getenv('VITA_PASSWORD', '')
    VITA_BASE_URL = os.getenv('VITA_BASE_URL', 'https://qa.vitawallet.io')

    # -----------------------------
    # Waits & Timeouts
    # -----------------------------
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '20'))
    TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '30'))

    @staticmethod
    def validate_config():
        """Validate that required environment variables are set"""
        required_vars = [
            'PETSTORE_BASE_URL',
            'APPIUM_SERVER_URL',
            'APP_PATH',
            'VITA_USER',
            'VITA_PASSWORD'
        ]
        missing_vars = [var for var in required_vars if not os.getenv(var)]

        if missing_vars:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )
