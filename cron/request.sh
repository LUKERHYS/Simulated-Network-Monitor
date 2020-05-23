#!/bin/bash
python3 /request.py $1
echo "$(date): $1 request sent" >> /var/log/cron.log 2>&1
