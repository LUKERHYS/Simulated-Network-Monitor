
from flask_crontab import Crontab
from keep_it_fresh import ping

crontab = Crontab()

# @crontab.job(minute="1", hour="0")
@crontab.job(crontab="1 * * * * python /Users/lukerhys/final_project.dun.dun.dun/cisco_app_server/keep_it_fresh.py")
def data_refresh_cron():
    print("Request complete!")


# cron = CronTab(user='root')
# job = cron.new(command='python keep_it_fresh.py')
# job.second.every(10)

# cron.write()

# cron = CronTab(crontab="""1 * * * * python /Users/lukerhys/final_project.dun.dun.dun/cisco_app_server/keep_it_fresh.py""")

