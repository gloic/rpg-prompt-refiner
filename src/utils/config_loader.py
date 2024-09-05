import argparse
import json
from os.path import join


class ConfigLoader:

    def __init__(self, config_filename: str = "default.json"):
        self.__config_filename = config_filename

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", default=self.__config_filename)
        return parser.parse_args()

    def load_config(self):
        args = self.parse_args()
        config_path = join("../config", args.config)

        with open(config_path, "r") as file:
            json_data = json.load(file)

        return json_data
