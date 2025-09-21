# Automation Framework - VITA

## Descripción
Framework de automatización para pruebas de API y mobile Android, desarrollado como parte del proceso de entrevista.

## Características
- Pruebas de API para PetStore (POST, GET, PUT, DELETE)
- Pruebas mobile Android para Vita Wallet con Appium
- Estructura modular y escalable
- Page Object Pattern para pruebas mobile
- Reportes con Allure y HTML

## Estructura del Proyecto

automation-framework-interview/
├── app/                                                  # Archivos binarios de aplicaciones móviles (ej. APKs para testing)
├── src/                                                  # Código fuente principal del framework
│   ├── api/                                              # Módulos para pruebas de APIs
│   │   ├── client/
│   │   │   └── petstore_client.py
│   │   ├── models/
│   │   │   └── pet.py
│   │   ├── schemas/
│   │   │   └── pet_schema.py
│   │   └── tests/                                        # Casos de prueba para API (positivos y negativos)
│   ├── mobile/                                           # Módulos para pruebas de mobile
│   │   ├── android/
│   │   │   ├── pages/                                    # Page Objects
│   │   │   ├── locators/                                 # Localizadores de elementos móviles
│   │   │   └── tests/                                    # Casos de prueba para API (positivos y negativos)
│   │   └── utils/
│   ├── utils/                                            # Utilidades generales (configuración, helpers, logger)
├── tests/                                                # Suites de pruebas integradoras
├── reports/                                              # Carpeta para reportes de ejecución
├── .env
├── conftest.py                                           # Configuración global de Pytest
├── pytest.ini                                            # Configuración de ejecución Pytest
├── requirements.txt                                      # Dependencias del proyecto
└── README.md




## Instalación
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `venv\Scripts\activate` 
4. Instalar dependencias: `pip install -r requirements.txt`

## Configuración
1. Configurar las variables de entorno según EL ambiente en el archivo `.env`

## Ejecución de Pruebas
- Todas las pruebas: `pytest`
- Solo API: `pytest src/api/tests/`
- Solo mobile: `pytest src/mobile/android/tests/`
- Con reporte HTML: `pytest --html=reports/report.html`
- Con Allure: `pytest --alluredir=reports/allure-results`

## Flujos Cubiertos
### API PetStore
- Creación, consulta, actualización y eliminación de mascotas
- Casos positivos y negativos para cada operación
- Validación de esquemas y respuestas

### Mobile Vita Wallet
- Login exitoso y fallido
- Navegación en la aplicación
- Validación de elementos UI

## Contacto
[Claudio Caceres] - [caceres.claudio@gmail.com]














README.md (sección de ejecución actualizada)
markdown
## Ejecución de Pruebas API

### Ejecutar todas las pruebas API
```bash
pytest src/api/tests/ -v
Ejecutar solo pruebas positivas
bash
pytest src/api/tests/ -m positive -v
Ejecutar solo pruebas negativas
bash
pytest src/api/tests/ -m negative -v
Ejecutar con reporte HTML
bash
pytest src/api/tests/ --html=reports/api-report.html --self-contained-html
Usar el script de ejecución
bash
python run_api_tests.py
Ejecutar pruebas específicas
bash
# Ejecutar una clase específica
pytest src/api/tests/test_pet_positive.py::TestPetPositive -v

# Ejecutar un test específico
pytest src/api/tests/test_pet_positive.py::TestPetPositive::test_create_pet -v