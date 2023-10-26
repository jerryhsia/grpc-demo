FROM jerry9916/centos:8

WORKDIR /root/grpc-demo

COPY *.py *.proto *.txt /root/grpc-demo/

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8886

ENTRYPOINT ["python3", "server.py"]