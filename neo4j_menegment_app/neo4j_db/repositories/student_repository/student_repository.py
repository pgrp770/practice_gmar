from dataclasses import asdict
from operator import itemgetter
from typing import List

import toolz as t
from neo4j_menegment_app.neo4j_db.database import driver
from neo4j_menegment_app.neo4j_db.models import Student, StudentTeacherClassRelation

def create_students(students: List[Student]):
    with driver.session() as session:
        query = """
        UNWIND $students AS student
        MERGE (s:Student{
            id:student.id    
        })
        """

        params = {
            "students": students
        }
        result = session.run(query, params).single()
        print(f"students were created")




def create_student(student: Student):
    with driver.session() as session:
        query = """
                    MERGE (s:Student{
                        id:$student_id     
                    })
                    RETURN s.id AS student_id
            """


        params = {
            "student_id": student.id
        }
        result = session.run(query, params).single()
        print(f"student with id {student.id} was created")
        return t.pipe(
            result,
            dict,
            itemgetter("student_id")
        )


def create_relation_student_class(relation: StudentTeacherClassRelation):
    with driver.session() as session:
        query = """
        MATCH (s:Student {id:$student_id}), (c:Class{id:$class_id})
        MERGE (s) - [rel: ENROLLED_IN {enrollment_date:$enrollment_date}] -> (c)
        return rel
        """

        params = {
            "student_id": relation.student_id,
            "class_id": relation.class_id,
            "enrollment_date": relation.enrollment_date
        }

        result = session.run(query, params).single()
        print(f"student {relation.student_id} was connected with class {relation.class_id}")
        return t.pipe(
            result,
            dict,
            itemgetter("rel")
        )


if __name__ == '__main__':
    # create_relation_student_class(StudentTeacherClassRelation(student_id="a", class_id="a", teacher_id="a", enrollment_date="test",relationship_type="test"))
    create_students([asdict(Student(id="0")), asdict(Student(id="1"))])