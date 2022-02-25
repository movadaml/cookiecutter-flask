"""Main application package."""

from .settings import BaseConfig, get_config_from_env
config: BaseConfig = get_config_from_env()