FROM debian
RUN apt-get update
RUN apt-get -y install python3 python3-pip

RUN mkdir app_server
WORKDIR /app_server
COPY . .
RUN chmod +x start.sh

RUN pip3 install sqlalchemy marshmallow-sqlalchemy asyncio websockets requests

EXPOSE 5001

ENTRYPOINT ["/bin/bash", "start.sh"]