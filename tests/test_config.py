import os

from app.config import get_config


def test_default_config():
    config = get_config()

    assert config["app_name"] == "Custodian Demo"
    assert config["debug"] is False
    assert config["port"] == 8000


def test_custom_port():
    os.environ["PORT"] = "9000"

    config = get_config()

    assert config["port"] == 9000

    del os.environ["PORT"]
