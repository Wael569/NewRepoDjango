from celery import shared_task
import time
from .pipelines import run_users_pipeline

@shared_task
def long_running_task():
    time.sleep(10)
    return "Task completed!"

@shared_task
def run_etl_CeleryApp():
    run_users_pipeline()