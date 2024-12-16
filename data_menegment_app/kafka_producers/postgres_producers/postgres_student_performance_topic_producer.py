from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
performance_topic = os.environ['POSTGRES_STUDENT_PERFORMANCE_TOPIC']

def produce_performance():
    produce(
        topic=performance_topic,
        key="test",
        value="test"
    )


if __name__ == '__main__':
    produce_performance()