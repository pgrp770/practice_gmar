from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
elastic_topic = os.environ['ELASTIC_TOPIC']

def produce_elastic(review):
    produce(
        topic=elastic_topic,
        key="review",
        value=review
    )
