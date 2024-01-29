from PyP100 import PyP100
from marvinChatter import marvinChat
import requests
import os
tv_ip = "192.168.2.6"
lamp_ip = "192.168.2.2"
light_ip= "192.168.2.2"
#http://192.168.2.3/cm?cmnd=Power%20Toggle

def turn_on(sen):
    return "άναψε" in sen or "άνοιξε"in sen or "ενεργοποιήσε"in sen 

def turn_off(sen):
    return "σβήσε"in sen or "κλείσε"in sen or "απενεργοποιήσε"in sen

def light(sen):
    return "φως" in sen or "φώτα" in sen

def lamp(sen):
    return "λάμπα" in sen or "λαμπατέρ" in sen or "φωτιστικό" in sen

def tv(sen):
    return "tv" in sen or "τηλεόραση" in sen

def play(sen):
    return "βάλε" in sen or "παίξε" in sen

def sound(sen):
    return "ήχο" in sen or "φωνή" in sen

def say(text,mChat):
    #mChat = marvinChat()
    mChat.textToSpeechGoogle(text, 'el')
    #test.textToSpeechGoogle(text,'el')
    print(text)

def do_the_math(text):
    u=""
    for i in text:
        if((ord(i)>=ord('0') and ord(i)<=ord('9')) or i=='-' or i=='+' or i=='*' or i=='/'):
            u=u+i
    return eval(u)

def nik_test(text,mchat):
    if(turn_on(text) and light(text)):
        say('ανάβω το φως',mchat)
        requests.get('http://'+light_ip+'/cm?cmnd=Power%20Toggle')

    if(turn_on(text) and lamp(text)):
        say('ανάβω το λαμπατέρ',mchat)
        try:
            p100 = PyP100.P100(lamp_ip, "nick8smirn@gmail.com", "Papadopoulos1!")
            p100.handshake()
            p100.login()
        except:
            pass
        p100.turnOn()

    if(turn_off(text) and light(text)):
        say('σβήνω το φως',mchat)
        requests.get('http://'+light_ip+'/cm?cmnd=Power%20Toggle')

    if(turn_off(text) and lamp(text)):
        say('σβήνω το λαμπατέρ',mchat)
        try:
            p100 = PyP100.P100(lamp_ip, "nick8smirn@gmail.com", "Papadopoulos1!")
            p100.handshake()
            p100.login()
        except:
            pass
        p100.turnOff()


    if(turn_on(text) and tv(text)):
        say('ανάβω την τηλεόραση',mchat)
        try:
            os.system("/Users/nikossmyrnakis/Desktop/adb connect "+tv_ip)
        except:
            pass
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_POWER")


    if(turn_off(text) and tv(text)):
        say('σβήνω την τηλεόραση',mchat)
        try:
            os.system("/Users/nikossmyrnakis/Desktop/adb connect "+tv_ip)
        except:
            pass
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_POWER")
    
    if(play(text) and "ant1" in text):
        say('βάζω το ant1',mchat)
        try:
            os.system("/Users/nikossmyrnakis/Desktop/adb connect "+tv_ip)
        except:
            pass
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_HOME")
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_HOME")
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_DPAD_RIGHT")
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_DPAD_RIGHT")
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_DPAD_CENTER")
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_7")

    if((turn_on(text) or turn_off(text)) and sound(text)):
        print("mute")
        try:
            os.system("/Users/nikossmyrnakis/Desktop/adb connect "+tv_ip)
        except:
            pass
        os.system("/Users/nikossmyrnakis/Desktop/adb shell input keyevent KEYCODE_MUTE")
    
    if("πόσο" in text and "κάνει" in text):
        say(str(do_the_math(text)),mchat)

    if("γκέι" in text or "gay" in text):
        say("δεν παίζει τον γκέι τετοια ωρα",mchat)