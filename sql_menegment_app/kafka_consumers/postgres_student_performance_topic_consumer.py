from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume

load_dotenv(verbose=True)
performance_topic = os.environ['POSTGRES_STUDENT_PERFORMANCE_TOPIC']

def consume_performance():
    consume(
        topic=performance_topic,
        function=lambda x: print(x.value)
    )


if __name__ == '__main__':
    consume_performance()