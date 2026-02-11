from django.http import JsonResponse
from .tasks import long_running_task

def start_task(request):
    task = long_running_task.apply_async(
        args=[],
        expires=30
    )

    return JsonResponse({
        "message": "Task started with apply_async!",
        "task_id": task.id
    })
