from data_menegment_app.config.file_dir import REVIEW_PATH
from data_menegment_app.kafka_producers.elasticsearch_producers.elasticsearch_review_producer import produce_elastic
from data_menegment_app.utils.csv_utils import produce_csv_in_chunks

if __name__ == '__main__':
    produce_csv_in_chunks(produce_elastic, REVIEW_PATH)
