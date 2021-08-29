import os
import time
import json
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

from kafka import KafkaProducer

from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData, DateTime

from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape 

DB_USERNAME = "ct_admin"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = 30518
DB_NAME = "geoconnections"

DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

db = create_engine(DATABASE_URI)

meta = MetaData(db)  


location_table = Table('location', meta,  
                       Column('person_id', String),
                       Column('coordinate', Geometry("POINT",  srid=4326)),
                       Column('creation_time', DateTime))

KAFKA_TOPIC = "test"
KAFKA_HOST = "localhost"
KAFKA_PORT = 30002

KAFKA_SERVER = f"{KAFKA_HOST}:{KAFKA_PORT}"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Get(self, request, context):

        locations = []

        with db.connect() as conn:
            location_select = location_table.select()
            result = conn.execute(location_select)
            for row in result:

                coordinate = to_shape(row.coordinate)

                locations.append(location_pb2.LocationMessage(
                    person_id=row.person_id,
                    longitude=coordinate.x,
                    latitude=coordinate.y,
                    creation_time=row.creation_time.strftime("%Y-%m-%d"),))

        result = location_pb2.LocationMessageList()
        result.locations.extend(locations)
        return result

    def Create(self, request, context):

        # Check database if such a person exists in database.
        # if not exits, push to kafka topic.

        request_value = {
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time,
        }

        json_message = json.dumps(request_value).encode()

        kafka_producer = producer

        kafka_producer.send(KAFKA_TOPIC, json_message)

        return location_pb2.Empty()


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
