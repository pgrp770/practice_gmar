from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume

load_dotenv(verbose=True)
life_style_topic = os.environ['POSTGRES_STUDENT_LIFE_STILE_TOPIC']

def consume_life_style():
    consume(
        topic=life_style_topic,
        function=lambda x: print(x.value)
    )


if __name__ == '__main__':
    consume_life_style()