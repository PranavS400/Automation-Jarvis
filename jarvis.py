from gtts import gTTS
import wikipedia
import time as tm
import webbrowser
import speech_recognition as sr
import pyaudio

import os
from datetime import date
from datetime import time
from datetime import datetime
def dating():
    today=date.today()
    week={1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday',7:'monday'}
    yes=today.weekday()
    return week[yes]
def time():
    rightnow = (datetime.time(datetime.now()))
    return rightnow

def reply(telling):
    language = 'en'
    speech = gTTS(text=telling, lang=language, slow=False)
    speech.save('text.mp3')
    os.system('start text.mp3')

def speak():
    y=sr.Recognizer()
    with sr.Microphone() as source:
        hear=y.listen(source)

        try:
            texting=y.recognize_google(hear)
            texting=texting.lower()
            return texting
        except:
            error=input('enter the command hear')

            return error
now=time()
to_day=dating()

reply('hi my name is macho ')
tm.sleep(5)
while True:
    reply('sir what next')
    tm.sleep(5)
    print('speak sir')
    experiment = speak()

    if experiment=='hello macho':
        reply("hello sir,today is "+to_day)
        reply('tell me sir what u need')
        tm.sleep(3)
        using=speak()

        if 'search google' in using:
            reply('what sir')
            tm.sleep(5)
            google=speak()

            print(google)
            reply('sir please wait')
            try:
                reply(wikipedia.summary(google))
            except:
                URL='https://www.google.com/search?q='
                webbrowser.open(URL)
            break
        elif 'youtube' in using:
            reply('what in youtube sir')
            tm.sleep(4)
            youtube=speak()
            while True:
                if 'my'in youtube:
                    url="https://www.youtube.com/watch?v=Thf60JU8E98"
                    webbrowser.open(url)
                    break

                else:
                    anyurl="https://www.youtube.com/"
                    webbrowser.open(anyurl)
                    break
            continue
        elif 'locate' in using:
            if using=='locate'+varplace:
                u="'https://www.google.com/maps/place/'+varplace"
                webbrowser.open(u)
            else:
                webbrowser.open('https://www.google.com')


        else:
            print('cant get u')



    else:
        reply('you are not pranav')
        tm.sleep(5)
        break


def listening():
    while True:
        reply(experiment)
        tm.sleep(5)
        break

