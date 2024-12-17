from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume

load_dotenv(verbose=True)
classes_topic = os.environ['POSTGRES_CLASSES_TOPIC']

def consume_classes():
    consume(
        topic=classes_topic,
        function=lambda x: print(x.value)
    )


if __name__ == '__main__':
    consume_classes()