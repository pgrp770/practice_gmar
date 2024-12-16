from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume

load_dotenv(verbose=True)
performance_topic = os.environ['POSTGRES_TEACHER_TOPIC']

def consume_teacher():
    consume(
        topic=performance_topic,
        function=lambda x: print(x.value)
    )


if __name__ == '__main__':
    consume_teacher()