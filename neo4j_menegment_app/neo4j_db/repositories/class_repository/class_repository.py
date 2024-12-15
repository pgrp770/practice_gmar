from operator import itemgetter
import toolz as t
from neo4j_menegment_app.neo4j_db.database import driver
from neo4j_menegment_app.neo4j_db.models import ClassModel


def create_class(class_model: ClassModel):
    with driver.session() as session:
        query = """
                    MERGE (c:Class{
                        id:$class_id     
                    })
                    RETURN c.id AS class_id
            """

        params = {
            "class_id": class_model.id
        }
        result = session.run(query, params).single()
        print(f"class with id {class_model.id} was created")
        return t.pipe(
            result,
            dict,
            itemgetter("class_id")
        )


if __name__ == '__main__':
    create_class(ClassModel(id='a'))