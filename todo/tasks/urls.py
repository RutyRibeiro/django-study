from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.tasksList, name='tasks-list'),
    path('yourName/<str:name>', views.yourName)
]
