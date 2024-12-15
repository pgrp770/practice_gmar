import csv

def read_csv_as_dict(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)  # Read each row as a dictionary
        for row in reader:
            yield row