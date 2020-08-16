#파이썬 음성인식 라이브러리 
import re
import speech_recognition 

#obtain audio from the microphone 
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print('Say something!')
    audio = recognizer.listen(source)

print('Google Speech Recognition thinks you said: ')
print(recognizer.recognize_google(audio))

#Recognize speech using google speech recognition 
words = recognizer.recognize_google(audio)

#Respond to speech 
matches = re.search('My name is (.*)', words)
if matches: 
    print(f'Hey, {matches[1]}')
else:
    print('Hey, you')