import speech_recognition as sr
import pyttsx3 as tts
import beepy

list = ['john','number','8','eight']
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
print("listening started...")
while(1):
	text = ""
	try:
		with sr.Microphone() as source:
			audio = r.listen(source,phrase_time_limit=1)
			text = r.recognize_google(audio)
			print(text)
	except sr.RequestError as e: 
        	print("Could not request results; {0}".format(e)) 
	except sr.UnknownValueError: 
        	print("unknown error occured")
	
	if any(word in text.lower() for word in list):
		print("alert...")	
		beepy.beep(sound=4)

