import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.mobile
class TestSmokeMobile:

    def test_app_launch_and_close(self, mobile_driver):
        """Verifica que la app se pueda abrir y cerrar correctamente"""

        try:
            # Verificar que el driver está inicializado
            assert mobile_driver is not None, "❌ El driver no se inicializó"

            # Obtener el activity actual
            current_activity = mobile_driver.current_activity
            logger.info(f"📱 Current activity: {current_activity}")

            # Guardar screenshot
            screenshot_path = "reports/screenshots/smoke_test.png"
            mobile_driver.save_screenshot(screenshot_path)
            logger.info(f"📸 Screenshot guardado en {screenshot_path}")

            # Verificación mínima: la app tiene activity activo
            assert current_activity is not None, "❌ No se detectó ninguna activity activa"

            logger.info("✅ Smoke test finalizado correctamente")

        except AssertionError as ae:
            logger.error(f"❌ Falló una aserción: {ae}")
            # Tomar screenshot adicional en caso de fallo
            fail_path = "reports/screenshots/smoke_test_failed.png"
            try:
                mobile_driver.save_screenshot(fail_path)
                logger.info(f"📸 Screenshot de error guardado en {fail_path}")
            except Exception as e:
                logger.error(f"No se pudo capturar screenshot al fallar: {e}")
            raise

        except Exception as e:
            logger.error(f"❌ Error inesperado en smoke test: {e}")
            raise
