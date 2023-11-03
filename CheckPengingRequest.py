import schedule
import time
import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv('API_URL')

def job():
    try:
        response = requests.get(api_url)
        if response.status_code == 200:

            data = response.json()    
            RequestCount = data["status"].get('pendingRequestCount', 'Field not found')
            RequestCount = str(RequestCount)
            current_time = datetime.datetime.now()
            current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Time : {current_time_str} \npendingRequestCount : {RequestCount}")

            if int(RequestCount) == 0:
                print(f"Program end at {current_time_str}") 
            
        else:
            print(f"Failed to fetch data from the API. Status code: {response.status_code}")
    except Exception as e:
        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Time : {current_time_str}\nAn error occurred : {e}")

schedule.every(5).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)