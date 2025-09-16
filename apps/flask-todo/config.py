"""Application configuration module.

Defines configuration classes to separate environment concerns.
Workshop-friendly: keeps defaults simple while demonstrating pattern.
"""
from __future__ import annotations

import os


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure-placeholder")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class DevConfig(BaseConfig):
    DEBUG = os.getenv("FLASK_DEBUG") == "1"


class TestConfig(BaseConfig):
    # Use in-memory DB for tests unless overridden
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")
    TESTING = True
    WTF_CSRF_ENABLED = False  # Typically disabled in unit tests for simplicity


class ProdConfig(BaseConfig):
    DEBUG = False


CONFIG_MAP = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": ProdConfig,
}


def get_config() -> type[BaseConfig]:
    env = os.getenv("FLASK_ENV") or os.getenv("ENV") or "development"
    return CONFIG_MAP.get(env, DevConfig)
