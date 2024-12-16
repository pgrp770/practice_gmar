from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume

load_dotenv(verbose=True)
teachers_topic = os.environ['NEO4J_TEACHERS_TOPIC']

def consume_teachers():
    consume(
        topic=teachers_topic,
        function=lambda x: print(x.value)
    )


if __name__ == '__main__':
    consume_teachers()