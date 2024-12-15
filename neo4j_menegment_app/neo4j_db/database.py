import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv(verbose=True)

neo4j_uri = os.environ.get("NEO4J_URL")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    uri=neo4j_uri,
    auth=(user,password)
)
if __name__ == '__main__':

    try:
        with driver.session() as session:
            session.run("RETURN 1")
        print("Connection successful!")
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        driver.close()