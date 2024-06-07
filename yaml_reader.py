import yaml
from pathlib import Path


def read_config():
    config_path = Path(__file__).parent / "config.yaml"
    with config_path.open() as file:
        return yaml.safe_load(file)
