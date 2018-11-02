import speech_recognition as sr
from os import system, name 

def  Speech_text():
	BING_KEY ='8c8841cff340458bbbe91195ab5f5b37'
	IBM_USERNAME='2b1d64dc-1b6d-401b-9e59-2147bf5ca9b2'
	IBM_PASSWORD='Y3CoHdDE4hcl'

	r = sr.Recognizer()
	r.energy_threshold= 400
	r.dynamic_energy_threshold = False
	with sr.Microphone() as source:
		audio = r.listen(source)
		
	text = r.recognize_google(audio,language='zh-TW')#list
	#text = r.recognize_bing(audio,key=BING_KEY,language='zh-TW')
	#text =r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD,language='zh-CN')
	
	try:
		print ("You said:"+text)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		pass
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

	return text
		 



if __name__ == '__main__':
	while True:
		a=Speech_text()
		print(type(a))





		'''
		# for windows 
		if name == 'nt': 
			_ = system('cls')  
		# for mac and linux(here, os.name is 'posix') 
		else: 
			_ = system('clear')
		''' 
