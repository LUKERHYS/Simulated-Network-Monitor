FROM debian
RUN apt-get update
RUN apt-get -y install cron python3 python3-pip
RUN pip3 install asyncio websockets 

ADD crontab /etc/cron.d/simple-cron

COPY . .

RUN chmod +x /request.sh /request.py
RUN chmod 0644 /etc/cron.d/simple-cron

RUN touch /var/log/cron.log

ENTRYPOINT ["/bin/bash", "/start.sh"]