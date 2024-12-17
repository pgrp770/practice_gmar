from dotenv import load_dotenv

import os

from data_menegment_app.config.file_dir import JSON_DATA_PATH
from data_menegment_app.utils.json_utils import read_json_file, produce_list_in_chunks
from kafka_settings.producer import produce

load_dotenv(verbose=True)
classes_topic = os.environ['CLASSES_TOPIC']

def produce_classes(data):
    produce(
        topic=classes_topic,
        key="teacher_list",
        value=data
    )


