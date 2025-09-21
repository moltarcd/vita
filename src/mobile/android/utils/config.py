# src/utils/config.py

import os

class Config:
    DEVICE_NAME = os.getenv("DEVICE_NAME", "emulator-5554")
    APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../app/VitaQA.apk"))
    APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://localhost:4723")