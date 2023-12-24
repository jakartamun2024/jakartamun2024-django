from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import ParticipantForm

# Create your views here.
def register_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the new participant to the database
            participant = form.save()

            # Here you can handle Cloudflare integration for file upload if needed

            return JsonResponse({'success': True, 'id': participant.id})
        else:
            # Return form errors if the form is not valid
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'error': 'Only POST method is allowed'}) 