import pytest
import os
import sys
from src.mobile.android.utils.appium_driver import AppiumDriver
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def run_mobile_tests():
    try:
        # Add src to path
        sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
        
        logger.info("Starting mobile tests...")
        
        # Run the tests
        pytest_args = [
            "-v",
            "--html=reports/mobile_test_report.html",
            "--self-contained-html",
            "src/mobile/android/tests/",
            "-m", "mobile"
        ]
        
        exit_code = pytest.main(pytest_args)
        
        return exit_code
        
    except Exception as e:
        logger.error(f"Error running mobile tests: {e}")
        return 1
    finally:
        # Clean up driver
        AppiumDriver.quit_driver()

if __name__ == "__main__":
    exit_code = run_mobile_tests()
    sys.exit(exit_code)