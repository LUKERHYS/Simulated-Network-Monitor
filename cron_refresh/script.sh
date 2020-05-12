lynx -dump http://172.19.0.1:5001/refresh
echo "$(date): executed script" >> /var/log/cron.log 2>&1
