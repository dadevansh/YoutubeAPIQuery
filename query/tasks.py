import time
from . import util, views
from celery import shared_task


@shared_task
def create_task(query):
    task_id = create_task.request.id
    util.query(query, task_id=task_id)
    return True