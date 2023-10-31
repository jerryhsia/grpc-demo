# grpc-demo

## start container

```
docker run -d --name="grpc-demo" -p 8886:8886 jerry9916/grpc-demo:latest python3 server.py
```

## test

```python3
import grpc
import simple_service_pb2
import simple_service_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:8886')
    stub = simple_service_pb2_grpc.SimpleServiceStub(channel)
    response = stub.SayHello(simple_service_pb2.HelloRequest(name='Jerry'))
    print(f"Server response: {response.message}")

if __name__ == '__main__':
    run()
```