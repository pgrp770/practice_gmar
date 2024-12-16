from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
elastic_topic = os.environ['ELASTIC_TOPIC']

def produce_new_member():
    produce(
        topic=elastic_topic,
        key="test",
        value="test"
    )


if __name__ == '__main__':
    produce_new_member()