from django.urls import path
from main_app.views import *
from admin.views import *
app_name = 'admin-page'

urlpatterns = [
    path('test/', test, name='test'),
    path('get-press/', get_press, name='test'),

]