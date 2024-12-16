from dataclasses import asdict
from datetime import datetime
from typing import List
import toolz as t

from elasticsearch_menegment_app.elastic_db.models.review import Review
from elasticsearch_menegment_app.elastic_db.repositories.repository_review import create_reviews


def parse_dict_to_review(review_dict:dict) -> Review:

    review_dict["score"] = int(review_dict["score"])
    review_dict["thumbs_up_count"] = int(review_dict["thumbs_up_count"])
    review_dict['date_time'] = datetime.strptime(review_dict['date_time'], '%d-%m-%Y %H:%M').isoformat()
    review_dict['student_id'] = int(review_dict['student_id'])
    return Review(**review_dict)


def from_list_to_actions(reviews) -> List[dict]:
    return [
        {
            "_index": "reviews",  # Specify the target index
            "_source": asdict(parse_dict_to_review(review))  # Convert the Review instance to a dictionary
        }
        for review in reviews
    ]


def main_flow_elastic_consumer(data):

    return t.pipe(
        data.value,
        from_list_to_actions,
        create_reviews
    )