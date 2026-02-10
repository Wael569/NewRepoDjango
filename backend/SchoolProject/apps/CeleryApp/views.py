from django.shortcuts import render
from .tasks import long_running_task
from django.http import HttpResponse

def ren(request):
    long_running_task.delay()
    return HttpResponse("Task has been started ...")