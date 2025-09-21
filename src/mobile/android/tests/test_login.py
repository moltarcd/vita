# src/mobile/android/tests/test_login.py

import pytest
from src.mobile.android.utils.appium_driver import get_driver
from src.mobile.android.pages.login_page import LoginPage
from src.data.users import VALID_USER  # Suponiendo que tienes datos de prueba

class TestLogin:

    def setup_method(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

    def test_login_successful(self):
        self.login_page.login(VALID_USER["username"], VALID_USER["password"])
        # Aquí podrías verificar que se cargó el dashboard, por ejemplo
        assert "Dashboard" in self.driver.page_source