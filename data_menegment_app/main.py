from data_menegment_app.config.file_dir import REVIEW_PATH, JSON_DATA_PATH
from data_menegment_app.kafka_producers.elasticsearch_producers.elasticsearch_review_producer import produce_elastic
from data_menegment_app.kafka_producers.producers.classes_topic_producer import produce_classes
from data_menegment_app.utils.csv_utils import produce_csv_in_chunks, read_csv_as_dict
from data_menegment_app.utils.json_utils import produce_list_in_chunks, read_json_file

if __name__ == '__main__':
    produce_list_in_chunks(produce_classes, read_json_file(JSON_DATA_PATH)["teachers"])

    produce_list_in_chunks(produce_elastic, read_csv_as_dict(REVIEW_PATH))
