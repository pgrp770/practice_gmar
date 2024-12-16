import csv


def read_csv_as_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Read each row as a dictionary
        for row in reader:
            yield row


def produce_csv_in_chunks(produce, file_path, chunk_size=100):
    buffer = []
    for row in read_csv_as_dict(file_path):
        buffer.append(row)
        if len(buffer) == chunk_size:
            produce(buffer)
            buffer = []

    if buffer:
        produce(buffer)
