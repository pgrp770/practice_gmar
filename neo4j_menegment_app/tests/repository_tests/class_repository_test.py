# import pytest
#
# from neo4j_menegment_app.neo4j_db.models import ClassModel
# from neo4j_menegment_app.neo4j_db.repositories.class_repository.class_repository import create_class
#
#
# @pytest.fixture(scope='module')
# def user():
#     class_to_insert = ClassModel(id="1234")
#     create_class(class_to_insert)
#     yield class_to_insert
#
#
# def test_create_class():
#     create_class()