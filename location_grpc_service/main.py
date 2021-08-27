import os
import time
import json
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

from kafka import KafkaProducer

KAFKA_TOPIC = "test"
KAFKA_HOST = "localhost"	
KAFKA_PORT = 30002

KAFKA_SERVER = f"{KAFKA_HOST}:{KAFKA_PORT}"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
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
