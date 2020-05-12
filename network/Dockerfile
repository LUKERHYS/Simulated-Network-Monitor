
FROM ubuntu
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

RUN mkdir Network_device_simulation
COPY ./Network_device_simulation ./Network_device_simulation

RUN pip3 install flask
RUN pip3 install flask-sqlalchemy
RUN pip3 install flask-marshmallow
RUN pip3 install marshmallow-sqlalchemy flask-cors

EXPOSE 5000

# CMD ["python3", "./Network_device_simulation/initdb.py"]
CMD ["python3", "./Network_device_simulation/app.py"]
