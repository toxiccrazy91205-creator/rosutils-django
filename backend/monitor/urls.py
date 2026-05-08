from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/message/', views.get_latest_message, name='get_latest_message'),
    path('api/send-command/', views.send_command, name='send_command'),
]
