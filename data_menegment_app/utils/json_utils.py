import json

from data_menegment_app.config.file_dir import JSON_DATA_PATH


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


if __name__ == '__main__':
    print(read_json_file(JSON_DATA_PATH)["teachers"])
