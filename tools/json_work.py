import json


def read_json(path: str):
    with open(path, 'r') as json_data:
        json_read = json.load(json_data)

    return json_read


def write_json(path: str, object):
    with open(path, "w") as json_data:
        json.dump(object, json_data)
