import time
from gtts import gTTS
from pygame import mixer
import tempfile
import pyttsx3
def speak_gTTS(sentence, lang='zh-tw', loop=1):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(loop)


def speak_pyttsx(sentence):
	engine = pyttsx3.init()
	engine.say(sentence)
	engine.runAndWait()
	# 朗读一次
	#engine.endLoop()

if __name__ == '__main__':
    while True:
        str=input('You wanna say:')
        speak_pyttsx(str)


