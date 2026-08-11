import configparser
from pathlib import Path

config = configparser.ConfigParser()
config_path = Path(__file__).parent.parent / "config" / "config.ini"
config.read(config_path)

URL = config["DEFAULT"]["URL"]
BROWSER = config["DEFAULT"]["browser"]

