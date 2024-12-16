from typing import List

from elasticsearch.helpers import bulk

from elasticsearch_menegment_app.elastic_db.database import elastic_client
from elasticsearch_menegment_app.elastic_db.models.review import Review


def create_review(review: Review):
    return elastic_client.index(index="reviews", body=review)


def create_reviews(reviews_actions: List[dict]):
    return bulk(elastic_client, reviews_actions)
