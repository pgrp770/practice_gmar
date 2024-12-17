from dotenv import load_dotenv
import os

from kafka_settings.consumer import consume
from neo4j_menegment_app.services.consumers_services.relation_consumer_service import main_flow_relation_consume

load_dotenv(verbose=True)
relations_topic = os.environ['NEO4J_RELATIONS_TOPIC']

def consume_relations():
    consume(
        topic=relations_topic,
        function=lambda x: main_flow_relation_consume(x.value)
    )



if __name__ == '__main__':
    consume_relations()
