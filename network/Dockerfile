FROM ubuntu
RUN apt-get update
RUN apt-get -y install python3 python3-pip curl

RUN mkdir Network_device_simulation
COPY ./Network_device_simulation ./Network_device_simulation

RUN pip3 install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask-cors

ADD start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "/start.sh"]