from operator import itemgetter
import toolz as t
from neo4j_menegment_app.neo4j_db.database import driver
from neo4j_menegment_app.neo4j_db.models import Teacher


def create_teacher(teacher: Teacher):
    with driver.session() as session:
        query = """
                    MERGE (t:Teacher{
                        id:$teacher_id     
                    })
                    RETURN t.id AS teacher_id
            """


        params = {
            "id": teacher.id
        }
        result = session.run(query, params).single()
        print(f"teacher_id with id {teacher.id} was created")
        return t.pipe(
            result,
            dict,
            itemgetter("teacher_id")
        )