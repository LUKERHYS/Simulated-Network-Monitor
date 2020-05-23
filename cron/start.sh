#!/bin/bash 
env | grep '^CRON_PASS' | cat - crontab > /etc/cron.d/simple-cron

cron && tail -f /var/log/cron.log