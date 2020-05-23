FROM ubuntu
RUN apt-get update
RUN apt-get -y install cron python3 python3-pip
RUN pip3 install asyncio websockets 

ADD crontab /etc/cron.d/simple-cron

COPY . .

RUN chmod +x /refresh.sh /refresh.py /clean.sh /clean.py
RUN chmod 0644 /etc/cron.d/simple-cron

RUN touch /var/log/cron.log
ENV CRON_PASS=../${CRON_PASS}
RUN env >> /etc/environment

ENTRYPOINT ["/bin/bash", "/start.sh"]