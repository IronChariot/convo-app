from django.urls import path
from . import views # import views.py from convo_app

urlpatterns = [
    path('', views.index, name='index'),
    path('get_audio', views.get_audio, name='get_audio'),
    path('send_audio', views.send_audio, name='send_audio'),
    path('send_message', views.send_message, name='send_message'),
    path('get_convo', views.get_convo, name='get_convo'),
]