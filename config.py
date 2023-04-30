#config.py
import yaml

class Config:
    """
    Class to handle YAML file.
    """
    def __new__(cls):
        with open('config.yml', 'r') as fd:
            return yaml.safe_load(fd)



