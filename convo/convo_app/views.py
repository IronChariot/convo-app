from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    topic = 'favorite foods'
    return render(request, 'convo_app/index.html', {'topic': topic})

def get_audio(request):
    logger.info("Got a get_audio request")
    logger.info(request)
    # Return an empty response
    return HttpResponse()

# @csrf_exempt
def send_audio(request, *args, **kwargs):
    audio_file: InMemoryUploadedFile = request.FILES.get('audio')

    if audio_file:
        # Here, call your transcription service with the audio_file
        # For instance, transcription_result = my_transcription_service(audio_file)

        # Assuming that transcription_result is a dictionary with necessary data
        return JsonResponse({ 'transcription_result': 'transcription_data_here' })

    return JsonResponse({ 'error': 'No file uploaded' }, status=400)

def send_message(request):
    logger.info("Got a send_message request")
    logger.info(request)
    return HttpResponse()