import json
import logging


def save_data(data: any, filename: str) -> None:
    try:
        with open(filename, "w") as file:
            json.dump(data, file)
    except Exception as e:
        logging.info("There was an error saving the data")


def load_data(filename: str) -> any:
    try:
        with open(filename, "r") as file:
            loaded_data = json.load(file)
            return loaded_data
    except Exception as e:
        logging.info("There was an error loading the data")

