from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume

load_dotenv(verbose=True)
new_member_topic = os.environ['ELASTIC_TOPIC']

def consume_members():
    consume(
        topic=new_member_topic,
        function=lambda x: print(x.value)
    )


if __name__ == '__main__':
    consume_members()