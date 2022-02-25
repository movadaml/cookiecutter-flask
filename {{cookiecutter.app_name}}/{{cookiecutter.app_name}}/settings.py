# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
# The idea is to make the app behave according to configuration preset selected by the APP_ENV environment variable,
# plus, add an option to override any configuration setting with a specific environment variable if required.

from .utils import ClassDict
import os


class BaseConfig(ClassDict):
    DEBUG: bool = False
    DATABASE_URL: str = "sqlite:////tmp/dev.db"
    GUNICORN_WORKERS: int = 1
    LOG_LEVEL: str = "info"
    SECRET_KEY: str = "not-so-secret"
    SEND_FILE_MAX_AGE_DEFAULT = 0
    BCRYPT_LOG_ROUNDS: int = 13
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    LOG_LEVEL: str = "warning"
    SEND_FILE_MAX_AGE_DEFAULT = 31556926


class TestConfig(BaseConfig):
    ENV = 'development'
    LOG_LEVEL: str = "debug"
    DEBUG = True


def _get_config(name: str) -> BaseConfig:
    config = globals().get(f"{name.title()}Config")
    assert config
    return config


# called from __init__
def get_config_from_env() -> BaseConfig:
    config = _get_config(os.environ.get("FLASK_ENV", "development"))
    config.update(**os.environ)
    return config
