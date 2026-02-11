from django.urls import path
from . import views


urlpatterns = [
    path('celerytest/', views.start_task, name='ren')
]