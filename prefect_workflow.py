import prefect
from prefect import task, Flow
from prefect.schedules import IntervalSchedule


import datetime


from extract_functions import extract_method
from telegram_message import send_message
from load_functions import load_to_sheet

import utils

# schedule to run every 12 hours
#schedule = IntervalSchedule(
#    start_date=datetime.datetime.utcnow() + datetime.timedelta(seconds=1),
#    interval=datetime.timedelta(hours=12))


schedule = IntervalSchedule(interval=datetime.timedelta(seconds=30))

@task
def extract():
    return extract_method()

@task
def send_telegram(data):
    send_message(data)
    return data

@task
def load(data):
    # store data into google sheet drive
    load_to_sheet(data)
    return data


with Flow("ex2", schedule=schedule) as flow:
    data = extract()
    data = send_telegram(data)
    data = load(data)

flow.run()

# Use prefect cloud
# flow.register(project_name="tutorial")
