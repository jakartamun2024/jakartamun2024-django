from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render, redirect

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login
from requests import Response

from django.contrib import messages  
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
import datetime


# Create your views here.
def test(request):
   
    return JsonResponse({"success": True, "message": "Your account has been successfully created!"})

def get_press(request):
    data = [
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        # Add more items if needed
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},

    ]
    
    return JsonResponse(data, safe=False)