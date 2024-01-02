import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over,thanks")

    try:
        print("Text: " + r.recognize_google(audio_text))
        print("Text: " + r.recognize_google(audio_text, language = "si-LK"))
    except:
        print("sorry,I did not get that")