import json
import time
import requests
from win32com.client import Dispatch

speak =  Dispatch("SAPI.SpVoice")


def speakLoud(str):
    speak.Speak(str)    


speakLoud("Heyy, I am your Jarvis. Getting news from internet ,  it might take time .  Wait for a while ")

res  =  requests.get("https://newsapi.org/v2/everything?q=tesla&from=2022-07-30&sortBy=publishedAt&apiKey=1538dcbbc63b4e24b909c673eae1e264");

parsed =  json.loads(res.text)

index =  1;
for data in parsed['articles']:
    speakLoud("News"+str(index))
    time.sleep(1)
    speakLoud(data['title'])
    index =  index+1


# print(parsed['articles'][0]['title'])


# print(res.text)


