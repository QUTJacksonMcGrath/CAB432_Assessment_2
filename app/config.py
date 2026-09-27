import os


def get_config():
    config = {
        "app_name": os.getenv(
            "APP_NAME",
            "Custodian Demo",
        ),

        "debug": os.getenv(
            "DEBUG",
            "false",
        ).lower() == "true",

        "port": int(
            os.getenv(
                "PORT",
                "8000",
            )
        ),
    }

    return config
