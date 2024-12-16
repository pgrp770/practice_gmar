from dotenv import load_dotenv
import os

from elasticsearch_menegment_app.elastic_db.repositories.repository_review import create_reviews
from elasticsearch_menegment_app.services.consumers_services.elastic_consumer_service import main_flow_elastic_consumer
from kafka_settings.consumer import consume

load_dotenv(verbose=True)
new_member_topic = os.environ['ELASTIC_TOPIC']

def consume_members():
    consume(
        topic=new_member_topic,
        function=main_flow_elastic_consumer
    )


if __name__ == '__main__':
    consume_members()