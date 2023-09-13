import os
import uuid
from elevenlabs import set_api_key, generate, save, play, Voice, VoiceSettings

# elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
# set_api_key(elevenlabs_api_key)

# Generate unique uuid
# uuid = generate()
# save(voice, uuid + ".wav")

def generate_audio(text):
    mikos_voice = Voice(
        voice_id='21m00Tcm4TlvDq8ikWAM',
        settings=VoiceSettings(stability=0.5, similarity_boost=0.75, style=0.0, use_speaker_boost=False)
    )
    audio = generate(text=text, voice=mikos_voice, model="eleven_multilingual_v2")
    return audio