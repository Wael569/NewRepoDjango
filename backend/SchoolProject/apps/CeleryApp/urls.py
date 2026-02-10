from django.urls import path, include
from . import views


urlpatterns = [
    path('celerytest/', views.long_running_task, name='ren')
]