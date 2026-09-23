import json
import os


DATA_FILE = "skillswap_data.json"


def create_empty_data():
    return {
        "students": [],
        "requests": [],
        "ratings": []
    }


def load_data():
    if not os.path.exists(DATA_FILE):
        return create_empty_data()

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)