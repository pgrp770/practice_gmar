from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
profile_topic = os.environ['POSTGRES_STUDENT_PROFILE_TOPIC']

def produce_profile():
    produce(
        topic=profile_topic,
        key="test",
        value="test"
    )


if __name__ == '__main__':
    produce_profile()