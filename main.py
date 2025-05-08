#importing speech recognition library , this library works as both offline and online

import speech_recognition as sr  #sr is variable

#r vanni varibale create garni tesma value katako rakhni vanda sr vanni library ko recognizer liyera rakhni

r= sr.Recognizer()

#importing the audio file and storing the audio text into audio_text

with sr.AudioFile('b.wav')as source:
    audio_text = r.listen(source)

#try,catch to handle the error
    try:
        text=r.recognize_google(audio_text)
        print('converting audio transcripts into text')
        print(text)

    except sr.UnknownValueError:
        print('could not understand audio')
    except  sr.RequestError as e:
        print(f"could not response the result: {e}")

    




