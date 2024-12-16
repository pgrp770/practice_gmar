from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume

load_dotenv(verbose=True)
profile_topic = os.environ['POSTGRES_STUDENT_PROFILE_TOPIC']

def consume_profile():
    consume(
        topic=profile_topic,
        function=lambda x: print(x.value)
    )


if __name__ == '__main__':
    consume_profile()