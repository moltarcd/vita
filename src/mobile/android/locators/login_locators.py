from appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:
    """Locators for Login page"""
    
    # Input fields
    EMAIL_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='emailInput']")
    PASSWORD_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='passwordInput']")
    
    # Buttons
    LOGIN_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='loginButton']")
    FORGOT_PASSWORD_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='Forgot Password?']")
    
    # Messages
    ERROR_MESSAGE = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='errorMessage']")
    SUCCESS_MESSAGE = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Welcome')]")
    
    # Other elements
    SHOW_PASSWORD_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='showPasswordButton']")