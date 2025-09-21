import pytest
import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from src.utils.config import Config
from src.utils.logger import setup_logger
from src.utils.helpers import safe_json_response
from src.api.models.pet import Pet
from src.mobile.android.utils.appium_driver import get_driver
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

logger = setup_logger(__name__)

# ==================== API FIXTURES ====================
@pytest.fixture(scope="session")
def petstore_client():
    """Fixture para el cliente de PetStore"""
    from src.api.clients.petstore_client import PetStoreClient
    Config.validate_config()
    return PetStoreClient()

@pytest.fixture
def valid_pet_data():
    """Fixture para datos válidos de mascota"""
    return Pet.create_valid_pet().to_dict()

@pytest.fixture
def invalid_pet_data():
    """Fixture para datos inválidos de mascota"""
    return Pet.create_invalid_pet().to_dict()

# ==================== MOBILE FIXTURES ====================
@pytest.fixture(scope="session")
def appium_driver():
    """Fixture de sesión para el driver de Appium"""
    from src.mobile.android.utils.appium_driver import AppiumDriver
    Config.validate_config()
    
    driver = None
    try:
        driver = AppiumDriver.get_driver()
        logger.info("✅ Appium driver initialized successfully")
        yield driver
    except Exception as e:
        logger.error(f"❌ Failed to initialize Appium driver: {e}")
        pytest.fail(f"Appium driver initialization failed: {e}")
    finally:
        if driver:
            driver.quit()
            logger.info("✅ Appium driver quit successfully")

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()            

@pytest.fixture
def mobile_driver(appium_driver):
    """Fixture de función para tests mobile con cleanup"""
    yield appium_driver
    # Cleanup después de cada test mobile
    try:
        # Volver al home o hacer reset de la app
        appium_driver.reset()
        logger.info("✅ App reset after test")
    except Exception as e:
        logger.warning(f"App reset failed: {e}")

@pytest.fixture
def login_page(mobile_driver):
    """Fixture para la página de login"""
    from src.mobile.android.pages.login_page import LoginPage
    return LoginPage(mobile_driver)

@pytest.fixture
def dashboard_page(mobile_driver):
    """Fixture para la página de dashboard"""
    from src.mobile.android.pages.dashboard_page import DashboardPage
    return DashboardPage(mobile_driver)

@pytest.fixture
def crypto_exchange_page(mobile_driver):
    """Fixture para la página de intercambio cripto"""
    from src.mobile.android.pages.crypto_exchange_page import CryptoExchangePage
    return CryptoExchangePage(mobile_driver)

@pytest.fixture
def logged_in_user(mobile_driver, login_page):
    """Fixture que realiza login y retorna dashboard page"""
    from src.mobile.android.pages.dashboard_page import DashboardPage
    
    try:
        # Intentar login
        login_page.login()
        
        # Verificar si el login fue exitoso
        dashboard_page = DashboardPage(mobile_driver)
        
        # Esperar a que cargue el dashboard
        import time
        time.sleep(3)
        
        # Verificar elementos del dashboard
        if dashboard_page.is_displayed(dashboard_page.locators.TOTAL_BALANCE):
            logger.info("✅ Login successful")
            return dashboard_page
        else:
            raise Exception("Login failed - Dashboard not loaded")
            
    except Exception as e:
        logger.error(f"❌ Login fixture failed: {e}")
        login_page.take_screenshot("login_failed")
        pytest.fail(f"Login failed: {e}")

@pytest.fixture
def on_crypto_page(logged_in_user):
    """Fixture que navega a la página de cripto"""
    try:
        logged_in_user.navigate_to_crypto()
        
        # Verificar que estamos en la página correcta
        if logged_in_user.is_displayed(logged_in_user.locators.EXCHANGE_BUTTON):
            logger.info("✅ Navigated to crypto page successfully")
            return logged_in_user
        else:
            raise Exception("Navigation to crypto page failed")
            
    except Exception as e:
        logger.error(f"❌ Navigation to crypto page failed: {e}")
        logged_in_user.take_screenshot("crypto_navigation_failed")
        pytest.fail(f"Navigation to crypto page failed: {e}")

# ==================== HOOKS ====================
def pytest_sessionstart(session):
    """Hook que se ejecuta al inicio de la sesión de tests"""
    logger.info("🚀 Starting test session")
    logger.info(f"Appium Server: {Config.APPIUM_SERVER_URL}")
    logger.info(f"App Path: {Config.APP_PATH}")

def pytest_sessionfinish(session, exitstatus):
    """Hook que se ejecuta al final de la sesión de tests"""
    logger.info("🏁 Test session finished")
    logger.info(f"Exit status: {exitstatus}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para tomar screenshots en fallos de tests mobile"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Tomar screenshot solo para tests mobile fallidos
        if "mobile_driver" in item.funcargs:
            driver = item.funcargs["mobile_driver"]
            try:
                screenshot_path = driver.save_screenshot(
                    f"reports/screenshots/failed_{item.name}.png"
                )
                logger.info(f"📸 Screenshot taken for failed test: {screenshot_path}")
            except Exception as e:
                logger.error(f"Failed to take screenshot: {e}")