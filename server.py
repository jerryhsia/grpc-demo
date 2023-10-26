import grpc
from concurrent import futures
import time

import simple_service_pb2
import simple_service_pb2_grpc

class SimpleService(simple_service_pb2_grpc.SimpleServiceServicer):
    def SayHello(self, request, context):
        return simple_service_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_service_pb2_grpc.add_SimpleServiceServicer_to_server(SimpleService(), server)
    
    hostAndPort = '[::]:8886';
    server.add_insecure_port(hostAndPort)
    server.start()
    print("Server started at "+hostAndPort)
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

