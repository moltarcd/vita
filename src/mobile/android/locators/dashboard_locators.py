from appium.webdriver.common.appiumby import AppiumBy

class DashboardLocators:
    """Locators for Dashboard page"""
    
    # Menu items
    CRYPTO_MENU_ITEM = (AppiumBy.XPATH, "//android.widget.TextView[@text='Crypto']")
    PROFILE_MENU_ITEM = (AppiumBy.XPATH, "//android.widget.TextView[@text='Profile']")
    SETTINGS_MENU_ITEM = (AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']")
    
    # Balance elements
    TOTAL_BALANCE = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='totalBalance']")
    ARS_BALANCE = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'ARS')]")
    USDT_BALANCE = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'USDT')]")
    
    # Quick actions
    BUY_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='Buy']")
    SELL_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='Sell']")
    EXCHANGE_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='Exchange']")