import json
import requests
from celery import Celery

celeryClient = Celery('tasks', 
    backend='redis://localhost',
    broker='redis://localhost')

@celeryClient.task
def post_activity(activity, url):
    try:
        r = requests.post(url, json=activity)
        if r.status_code == 201:
            print(f"Post new activity SUCCESS at {url}")
            print(r.text)
            print(json.loads(r.text))
        else:
            print(f"Post new activity FAILURE: {r.text}")
    except requests.exceptions.RequestException:
        print(f"Could not connect to activity log service at {url}")
