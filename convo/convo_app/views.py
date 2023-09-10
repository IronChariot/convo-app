from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
import logging
import whisper
import os
import uuid
import json
from .gpt import set_system_message, get_response, get_topic, convo

logger = logging.getLogger(__name__)
model = whisper.load_model("medium")
audio_dict = {}
# Remove all existing .wav files
for file in os.listdir("."):
    if file.endswith(".wav"):
        os.remove(file)

# Create your views here.
def index(request):
    topic = get_topic()
    first_message = set_system_message()
    return render(request, 'convo_app/index.html', {'topic': topic, 'first_message': first_message})

def get_audio(request):
    logger.info("Got a get_audio request")
    # Get the message_text from the request
    body_data = json.loads(request.body.decode('utf-8'))
    message_text = body_data.get('message_text')
    message_text_trimmed = message_text.strip()

    # Get the uuid from the audio_dict
    uuid = audio_dict.get(message_text_trimmed)
    # Get the audio file from the uuid
    audio_file = open(uuid + ".wav", "rb")
    # Return the audio file in the response
    response = HttpResponse(audio_file, content_type="audio/wav")
    return response

# @csrf_exempt
def send_audio(request, *args, **kwargs):
    audio_file: InMemoryUploadedFile = request.FILES.get('audio')

    if audio_file:
        # Save the audio file as [random uuid].wav
        new_uuid = str(uuid.uuid4())
        with open(new_uuid + '.wav', 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)
        result = model.transcribe(new_uuid + ".wav", language="ja")
        # Save the uuid against the string that the model returns in the audio_dict, so we can find the file later
        transcript_trimmed = result["text"].strip()
        audio_dict[transcript_trimmed] = new_uuid

        # Assuming that transcription_result is a dictionary with necessary data
        return JsonResponse({ 'transcription_result': result["text"] })

    return JsonResponse({ 'error': 'No file uploaded' }, status=400)

def send_message(request):
    logger.info("Got a send_message request")
    body_data = json.loads(request.body.decode('utf-8'))
    message_text = body_data.get('message_text')
    message_text_trimmed = message_text.strip()
    response = get_response(message_text_trimmed)
    return JsonResponse({ 'response': response })

def get_convo(request):
    logger.info("Got a get_convo request")
    # Turn the convo.list into just json
    convo_json = json.dumps(convo.list)
    return JsonResponse({ 'convo': convo_json })