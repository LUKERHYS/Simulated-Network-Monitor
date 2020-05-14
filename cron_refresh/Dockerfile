FROM ubuntu
RUN apt-get update
RUN apt-get -y install cron python3 python3-pip
RUN pip3 install asyncio websockets 

ADD crontab /etc/cron.d/simple-cron

# Add shell script and grant execution rights
ADD script.sh /script.sh
RUN chmod +x /script.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/simple-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log