from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume

load_dotenv(verbose=True)
relations_topic = os.environ['NEO4J_RELATIONS_TOPIC']

def consume_relations():
    consume(
        topic=relations_topic,
        function=lambda x: print(x.value)
    )


if __name__ == '__main__':
    consume_relations()