from elasticsearch_menegment_app.elastic_db.database import elastic_client


def test_elastic_connection():
    assert elastic_client.ping()
