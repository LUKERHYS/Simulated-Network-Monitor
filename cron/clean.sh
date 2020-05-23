#!/bin/bash
python3 /clean.py
echo "$(date): Clean request sent" >> /var/log/cron.log 2>&1