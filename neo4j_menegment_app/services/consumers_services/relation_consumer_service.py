from neo4j.graph import Relationship

from neo4j_menegment_app.neo4j_db.models import Student, ClassModel, Teacher, StudentTeacherClassRelation
from neo4j_menegment_app.neo4j_db.repositories.class_repository.class_repository import create_class
from neo4j_menegment_app.neo4j_db.repositories.student_repository.student_repository import create_student, \
    create_relation_student_class
from neo4j_menegment_app.neo4j_db.repositories.teacher_repository.teacher_repository import create_teacher, \
    create_relation_teacher_class


def insert_relation_dict(relation_dict):
    relation = StudentTeacherClassRelation(**relation_dict)
    create_student(Student(id=relation.student_id))
    create_class(ClassModel(id=relation.class_id))
    create_teacher(Teacher(id=relation.teacher_id))
    create_relation_student_class(relation)
    create_relation_teacher_class(relation)

def main_flow_relation_consume(relations):
    [insert_relation_dict(relation) for relation in relations]
if __name__ == '__main__':
    a = {'student_id': '668', 'class_id': 'BIO-260', 'teacher_id': 'BIO-9971', 'enrollment_date': '2024-12-12', 'relationship_type': 'ENROLLED_IN'}


