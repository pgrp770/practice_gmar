import os
from dotenv import load_dotenv
import faust


# Load environment variables
load_dotenv(verbose=True)

# Faust app for stream processing
app = faust.App(
    'teachers_streaming',  # App name
    broker=os.environ['BOOTSTRAP_SERVERS'],  # Kafka broker
    value_serializer='json'  # Message value format
)

# Define a Kafka topic to consume from
teacher_topic = app.topic(os.environ["TEACHER_TOPIC"])

processed_teacher_topic_neo4j = app.topic(os.environ["NEO4J_TEACHERS_TOPIC"])
processed_teacher_topic_postgres = app.topic(os.environ["POSTGRES_TEACHER_TOPIC"])


# Stream processing agent
@app.agent(teacher_topic)
async def process_person(messages):
    async for message in messages:


        await processed_teacher_topic_neo4j.send(value={"id":message["id"]})
        await processed_teacher_topic_postgres.send(value=message)

if __name__ == '__main__':
    # Run Faust in one thread
    app.main()
