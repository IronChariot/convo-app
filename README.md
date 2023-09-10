# convo-app
An app that combines the Whisper API, GPT-3.5-Turbo API and Elevenlabs API to help you practice speaking a language with low stress. Runs as a local web app in django, because I wanted to learn django and I can make use of my knowledge of JS and CSS.

Your own API keys for the three services should be added in a file called 'api_keys.txt' when running the server locally.

# Install & Run
Create a python env in the root directory, and install django, openai-whisper and chatterstack. Then, run the django server with python manage.py runserver in the convo directory.