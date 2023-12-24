from django.urls import path
from main_app.views import *

app_name = 'main'

urlpatterns = [
    path('register/', register_participant, name='register_participant'),
]