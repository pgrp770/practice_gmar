from datetime import datetime
from dataclasses import asdict
from typing import List

from elasticsearch.helpers import bulk

from elasticsearch_menegment_app.elastic_db.database import elastic_client
from elasticsearch_menegment_app.elastic_db.models.review import Review


def create_review(review: Review):
    return elastic_client.index(index="reviews", body=review)


def create_reviews(reviews: List[Review]):
    actions = [
        {
            "_index": "reviews",  # Specify the target index
            "_source": asdict(review)  # Convert the Review instance to a dictionary
        }
        for review in reviews
    ]
    return bulk(elastic_client, actions)


if __name__ == '__main__':
    reviews = [
    Review(
        review_id="test",
        content="test",
        score=1,
        thumbs_up_count=1,
        review_created_version="d",
        date_time=datetime.now(),
        app_version="test",
        student_id=2
    ),
    Review(
        review_id="test",
        content="test",
        score=1,
        thumbs_up_count=1,
        review_created_version="d",
        date_time=datetime.now(),
        app_version="test",
        student_id=3
    )

    ]
    print(create_reviews(reviews))

"""
   review_id: str
   content: str
   score: int
   thumbs_up_count: int
   review_created_version: str
   date_time: datetime
   app_version: str
   student_id: int"""
