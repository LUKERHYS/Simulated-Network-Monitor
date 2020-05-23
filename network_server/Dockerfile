FROM debian
RUN apt-get update
RUN apt-get -y install python3 python3-pip curl

RUN mkdir network_server
WORKDIR /network_server
COPY . .
RUN chmod +x start.sh

RUN pip3 install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask-cors


EXPOSE 5000

ENTRYPOINT ["/bin/bash", "start.sh"]