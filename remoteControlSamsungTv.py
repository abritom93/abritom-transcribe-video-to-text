import sys
import os
import speech_recognition as sr
from samsungtvws import SamsungTVWS

recognizer = sr.Recognizer()

sys.path.append('../')

token_file = os.path.dirname(os.path.realpath(__file__)) + '/tv-token.txt'

tv = SamsungTVWS(host='192.168.1.136', port=8002, token_file=token_file)


def shutdown():
    tv.shortcuts().power()

def volume_down(times):
    if times == 0:
        tv.shortcuts().volume_down()
        return

    for i in times:
        tv.shortcuts().volume_down()

def volume_up(times):
    if times == 0:
        tv.shortcuts().volume_up()
        return

    for i in times:
        tv.shortcuts().volume_up()


def open_application(application):
    match application:
        case 'YouTube':
            tv.run_app('111299001912')
        case 'Netflix':
            tv.run_app('11101200001')
        case _:
            print("App no entrada")


def execute_action(action):
    match action:
        case 'apagar':
            shutdown()
        case 'subir volumen':
            volume_up([3])
        case 'bajar volumen':
            volume_down([3])
        case 'YouTube':
            open_application('YouTube')
        case 'Netflix':
            open_application('Netflix')
        case _:
            print('No lo he entendido')


while True:
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = recognizer.record(source, duration=6)
        print("Recognizing...")
        # convert speech to text
        text = recognizer.recognize_google(audio_data, language='es-ES')
        print(text)
        execute_action(text)
