# pip install pyttsx3
import pyttsx3
txt_spc=pyttsx3.init()                                        #we use init class to convert text into speech
text=input('enter the text...\n')
voices=txt_spc.getProperty('voices')                #to identify the voices(we got 2 voices)
for voice in voices:
    print('ID:',voice.id)
txt_spc.setProperty('voice',voices[1].id)           #we set the voices we need
txt_spc.say(text)
txt_spc.runAndWait()