from celery import shared_task
import time

@shared_task
def long_running_task():
    time.sleep(10) # naamlou task
    print("Task completed!")  # print fil console log to verify
    return "Task completed!"
