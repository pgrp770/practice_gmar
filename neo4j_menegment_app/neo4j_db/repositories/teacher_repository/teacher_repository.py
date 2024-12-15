from operator import itemgetter
import toolz as t
from neo4j_menegment_app.neo4j_db.database import driver
from neo4j_menegment_app.neo4j_db.models import Teacher, StudentTeacherClassRelation, Student


def create_teacher(teacher: Teacher):
    with driver.session() as session:
        query = """
                    MERGE (t:Teacher{
                        id:$teacher_id     
                    })
                    RETURN t.id AS teacher_id
            """


        params = {
            "teacher_id": teacher.id
        }
        result = session.run(query, params).single()
        print(f"teacher_id with id {teacher.id} was created")
        return t.pipe(
            result,
            dict,
            itemgetter("teacher_id")
        )


def create_relation_teacher_class(relation: StudentTeacherClassRelation):
    with driver.session() as session:
        query = """
        MATCH (t:Teacher {id:$teacher_id}), (c:Class{id:$class_id})
        MERGE (t) - [rel: ENROLLED_IN {enrollment_date:$enrollment_date}] -> (c)
        return rel
        """

        params = {
            "teacher_id": relation.teacher_id,
            "class_id": relation.class_id,
            "enrollment_date": relation.enrollment_date
        }

        result = session.run(query, params).single()
        print(f"teacher {relation.teacher_id} was connected with class {relation.class_id}")
        return t.pipe(
            result,
            dict,
            itemgetter("rel")
        )


if __name__ == '__main__':
    create_relation_teacher_class(StudentTeacherClassRelation(student_id="a", class_id="a", teacher_id="a", enrollment_date="test", relationship_type="test"))
    create_teacher(Teacher("a"))