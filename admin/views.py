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
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport=============================================================================================================================================!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        # Add more items if needed
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
        {"image_link": 'https://akcdn.detik.net.id/community/media/visual/2020/04/04/9213bb7d-7f5e-4792-bdef-49356d5fd571_169.jpeg?w=700&q=90','title':'Pesawat Tabrakan di Haneda Airport!', 'link': "https://news.detik.com/internasional/d-7120881/pesawat-japan-airlines-tabrakan-dengan-pesawat-lain-di-bandara-haneda"},
    ]
    
    return JsonResponse(data, safe=False)
def get_detail(request):
    data = {
      "full_name_delegate": "Alex Smith",
      "email": "alex.smith@example.com",
      "status": "Head Delegate",
      "institution": "Global Model United Nations",
      "nationality": "Indonesian",
      "age": 25,
      "contact_number": "+628123456789",
      "line_id": "alexsmithline",
      "first_council_preference": "Security Council",
      "country_first_council": "France",
      "second_council_preference": "Human Rights Council",
      "country_second_council": "Brazil",
      "third_council_preference": "Economic and Financial Committee",
      "country_third_council": "India",
      "previous_mun_experience":
          "Participated in 3 MUN conferences previously.",
      "dietary_restriction": "No restrictions",
      "special_medical_condition": "None",
      "accom_status": "Non-Accommodated",
      "proof_of_transfer":
          "https://miro.medium.com/v2/resize:fit:828/format:webp/0*YvMogQLKcU-kHv6v"
    }
    return JsonResponse(data, safe=False)