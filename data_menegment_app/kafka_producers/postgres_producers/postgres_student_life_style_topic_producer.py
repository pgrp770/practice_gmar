from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
life_style_topic = os.environ['POSTGRES_STUDENT_LIFE_STILE_TOPIC']

def produce_life_style():
    produce(
        topic=life_style_topic,
        key="test",
        value="test"
    )


if __name__ == '__main__':
    produce_life_style()