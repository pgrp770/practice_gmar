from operator import itemgetter
import toolz as t
from neo4j_menegment_app.neo4j_db.database import driver
from neo4j_menegment_app.neo4j_db.models import Student


def create_teacher(student: Student):
    with driver.session() as session:
        query = """
                    MERGE (s:Student{
                        id:$student_id     
                    })
                    RETURN s.id AS student_id
            """


        params = {
            "id": student.id
        }
        result = session.run(query, params).single()
        print(f"student with id {student.id} was created")
        return t.pipe(
            result,
            dict,
            itemgetter("student_id")
        )