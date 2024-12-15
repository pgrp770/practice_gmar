import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
load_dotenv(verbose=True)
client = Elasticsearch(os.environ["ELASTIC_URL"])

if __name__ == '__main__':

    if client.ping():
        print("Connected to Elasticsearch!")
    else:
        print("Connection failed.")