"""
Basic mobile app verification tests
"""
import pytest
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.mobile
class TestAppVerification:
    """Basic app verification tests"""
    
    def test_app_launch(self, mobile_driver):
        """Test that the app launches successfully"""
        # Verify app is launched by checking package name
        current_package = mobile_driver.current_package
        assert current_package == "io.vitawallet.wallet", \
            f"Expected package io.vitawallet.wallet, got {current_package}"
    
    def test_app_activity(self, mobile_driver):
        """Test that the correct activity is launched"""
        current_activity = mobile_driver.current_activity
        assert "MainActivity" in current_activity, \
            f"Expected MainActivity, got {current_activity}"
    
    def test_app_screenshot(self, mobile_driver):
        """Test taking screenshot capability"""
        screenshot_path = mobile_driver.save_screenshot("reports/screenshots/app_launch.png")
        assert screenshot_path is not None
        print(f"Screenshot saved: {screenshot_path}")