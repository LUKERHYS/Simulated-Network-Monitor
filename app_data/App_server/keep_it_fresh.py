import requests
import schedule
import time

def ping():
    requests.get('http://localhost:5001/refresh')
    print("Request data...request complete")

schedule.every(10).seconds.do(ping)
counter = 0
while counter < 5:
    schedule.run_pending()
    time.sleep(5)
    counter += 1


    ##commit and push it