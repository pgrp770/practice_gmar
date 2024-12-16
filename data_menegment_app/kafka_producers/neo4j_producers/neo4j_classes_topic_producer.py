from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
classes_topic = os.environ['NEO4J_CLASSES_TOPIC']

def produce_classes():
    produce(
        topic=classes_topic,
        key="test",
        value="test"
    )


if __name__ == '__main__':
    produce_classes()