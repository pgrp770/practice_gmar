from datetime import datetime
from dataclasses import asdict
from elasticsearch_menegment_app.elastic_db.database import elastic_client
from elasticsearch_menegment_app.elastic_db.models.review import Review


def create_review(review:Review):
    return elastic_client.index(index="reviews",body=review)


if __name__ == '__main__':
    review = Review(
        review_id="test",
        content="test",
        score=1,
        thumbs_up_count=1,
        review_created_version="d",
        date_time=datetime.now(),
        app_version="test",
        student_id=1
    )
    print(create_review(asdict(review)))


"""
   review_id: str
   content: str
   score: int
   thumbs_up_count: int
   review_created_version: str
   date_time: datetime
   app_version: str
   student_id: int"""