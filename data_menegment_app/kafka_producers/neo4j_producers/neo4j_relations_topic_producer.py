from dotenv import load_dotenv

import os

from data_menegment_app.config.file_dir import JSON_DATA_PATH
from data_menegment_app.services.producers_services.batch_produce import produce_chunks
from data_menegment_app.utils.json_utils import read_json_file
from kafka_settings.producer import produce

load_dotenv(verbose=True)
relations_topic = os.environ['NEO4J_RELATIONS_TOPIC']

def produce_relations(relations):
    produce(
        topic=relations_topic,
        key="relations_list",
        value=relations
    )


if __name__ == '__main__':
    produce_chunks( read_json_file(JSON_DATA_PATH)["relationships"],produce_relations, 1000)