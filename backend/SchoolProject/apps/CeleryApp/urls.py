from django.urls import path, include
from . import views


urlpatterns = [
    path('celerytest/', views.ren, name='ren')
]