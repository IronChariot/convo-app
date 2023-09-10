import chatterstack
import openai
import os

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
model_to_use = "gpt-3.5-turbo"

topic_convo = chatterstack.Chatterstack()
convo = chatterstack.Chatterstack()
topic = ""

def get_topic():
    global topic
    # Get list of previous topics from file
    with open("topics.txt", "r") as f:
        prev_topics = f.readlines()

    # Create a prompt for getting a new topic
    prompt = "The following is a list of topics that have been used in previous conversations with a language learning beginner:\n"
    for prev_topic in prev_topics:
        prompt += f"- {prev_topic}\n"
    prompt += "Please enter a new topic for today's conversation in the same format as the above, with nothing else except the topic name, as your response will be fed into an algorithm that expects to get just the topic."
    topic_convo.add("user", prompt)
    topic_convo.send_to_bot(model=model_to_use)
    topic = topic_convo.last_message
    # Save the topic to a new line in the file
    with open("topics.txt", "a") as f:
        f.write(topic + "\n")

    return topic

def set_system_message():
    # Create the system message
    message_text = f"You will act as a conversation partner for Japanese language practice. The user, named Sam, is still a beginner, knowing between 2000 and 3000 words, so keep the vocabulary and grammar reasonably simple, maybe at a JLPT N5 or N4 level. You will be roleplaying as Sam's friend Miko, who only speaks Japanese. Sam will be using AI to transcribe what he says, so if something seems wrong in his messages, please ask clarifying questions, in case it was the AI that transcribed what he said incorrectly. The topic for today is '{topic}'. Please assume greetings have already been made, so there is no need to say hello, and create your first message as Miko, saying something or asking Sam a question about the topic. Only use hiragana, katakana, and kanji, and no romaji. Do not ask multiple questions in one message."
    convo.add("system", message_text)
    convo.send_to_bot(model=model_to_use)
    reply = convo.last_message
    return reply

def get_response(message_text):
    convo.add("user", message_text)
    # Get the response from the model
    convo.send_to_bot(model=model_to_use)
    response = convo.last_message
    # Return the response
    return response