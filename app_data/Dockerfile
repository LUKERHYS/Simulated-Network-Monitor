FROM ubuntu
RUN apt-get update
RUN apt-get -y install python3 python3-pip


RUN mkdir App_server
COPY ./App_server ./App_server

RUN pip3 install sqlalchemy marshmallow-sqlalchemy asyncio websockets requests

ADD start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 5001


ENTRYPOINT ["/bin/bash", "/start.sh"]