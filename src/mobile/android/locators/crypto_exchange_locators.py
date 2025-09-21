from appium.webdriver.common.appiumby import AppiumBy

class CryptoExchangeLocators:
    """Locators for Crypto Exchange page"""
    
    # Currency selection
    FROM_CURRENCY_DROPDOWN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='fromCurrency']")
    TO_CURRENCY_DROPDOWN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='toCurrency']")
    
    # Currency options
    CURRENCY_OPTION_ARS = (AppiumBy.XPATH, "//android.widget.TextView[@text='ARS']")
    CURRENCY_OPTION_USDT = (AppiumBy.XPATH, "//android.widget.TextView[@text='USDT']")
    
    # Amount inputs
    AMOUNT_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='amountInput']")
    ESTIMATED_AMOUNT = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='estimatedAmount']")
    
    # Buttons
    CONTINUE_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='Continue']")
    CONFIRM_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='Confirm']")
    CANCEL_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='Cancel']")
    
    # Review screen
    EXCHANGE_RATE = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='exchangeRate']")
    FEE_AMOUNT = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='feeAmount']")
    TOTAL_AMOUNT = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='totalAmount']")
    
    # Success/Error messages
    SUCCESS_MESSAGE = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'successful')]")
    ERROR_MESSAGE = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='errorMessage']")