from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
relations_topic = os.environ['NEO4J_RELATIONS_TOPIC']

def produce_relations():
    produce(
        topic=relations_topic,
        key="test",
        value="test"
    )


if __name__ == '__main__':
    produce_relations()