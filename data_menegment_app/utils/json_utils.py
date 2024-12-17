import json

from data_menegment_app.config.file_dir import JSON_DATA_PATH


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data
def produce_list_in_chunks(produce, data_list, chunk_size=4):
    buffer = []
    for row in data_list:

        buffer.append(row)
        if len(buffer) == chunk_size:
            produce(buffer)
            buffer = []


