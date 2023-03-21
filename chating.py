import speech_recognition as sr
import asyncio

r=sr.Recognizer()

async def recoding():

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("질문하세요!")
        audio=r.listen(source,30)

    try:
        transcript=r.recognize_google(audio, language="ko-KR")
        return transcript
    except sr.UnknownValueError:
        return "다시 말해주세요."
    except sr.RequestError as e:
        return  "작동되지 않았습니다. 오류코드: {0}".format(e)

import os
import openai
from googletrans import Translator

openai.api_key = "API_KEY"

async def chat(content):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=content,
    max_tokens=4000,
    temperature=0
    )
    return response["choices"][0]["text"].strip()

async def start():
    user = await recoding()
    print(user)
    
    result = await chat(user)
    print('========================')
    return user,result
    print('========================')