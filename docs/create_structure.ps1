# ===============================================
# Script para crear estructura de proyecto
## ===============================================

# Carpeta raíz
$root = "automation-framework-vita"

# Crear carpeta raíz
New-Item -ItemType Directory -Force -Path $root | Out-Null

# Subcarpetas
$folders = @(
    "app",
    "src\api\clients",
    "src\api\models",
    "src\api\schemas",
    "src\api\tests",
    "src\mobile\android\pages",
    "src\mobile\android\locators",
    "src\mobile\android\tests",
    "src\mobile\android\utils",
    "src\mobile\utils",
    "src\utils",
    "src\data",
    "tests",
    "reports"
)

foreach ($f in $folders) {
    $path = Join-Path $root $f
    New-Item -ItemType Directory -Force -Path $path | Out-Null
}

# Archivos
$files = @(
    "app\vita-wallet-qa.apk",
    "src\api\clients\petstore_client.py",
    "src\api\models\pet.py",
    "src\api\schemas\pet_schema.py",
    "src\api\tests\__init__.py",
    "src\api\tests\test_pet_positive.py",
    "src\api\tests\test_pet_negative.py",
    "src\mobile\android\pages\base_page.py",
    "src\mobile\android\pages\login_page.py",
    "src\mobile\android\pages\dashboard_page.py",
    "src\mobile\android\pages\crypto_exchange_page.py",
    "src\mobile\android\locators\login_locators.py",
    "src\mobile\android\locators\dashboard_locators.py",
    "src\mobile\android\locators\crypto_exchange_locators.py",
    "src\mobile\android\tests\__init__.py",
    "src\mobile\android\tests\test_crypto_exchange.py",
    "src\mobile\android\utils\appium_driver.py",
    "src\utils\config.py",
    "src\utils\logger.py",
    "src\utils\helpers.py",
    "src\data\test_data.py",
    "src\data\users.py",
    ".env.example",
    ".gitignore",
    "conftest.py",
    "pytest.ini",
    "requirements.txt",
    "README.md"
)

foreach ($file in $files) {
    $path = Join-Path $root $file
    New-Item -ItemType File -Force -Path $path | Out-Null
}

Write-Host "✅ Estructura creada en: $root"
