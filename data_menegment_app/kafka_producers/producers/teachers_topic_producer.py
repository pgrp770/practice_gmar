from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
teachers_topic = os.environ['TEACHER_TOPIC']

def produce_teachers():
    produce(
        topic=teachers_topic,
        key="test",
        value={"id":"id", "test":"test"}
    )


if __name__ == '__main__':
    produce_teachers()