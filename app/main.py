from flask import Flask

from app.config import get_config


app = Flask(__name__)


@app.route("/")
def index():
    config = get_config()

    return {
        "message": f"Welcome to {config['app_name']}",
        "debug": config["debug"],
    }


if __name__ == "__main__":
    config = get_config()

    app.run(
        host="0.0.0.0",
        port=config["port"],
        debug=config["debug"],
    )
