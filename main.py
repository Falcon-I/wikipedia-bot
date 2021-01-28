import pyttsx3
import wikipedia as w
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty("rate", 200)
engine.setProperty("voice", voice_id)
def speak(text):
    engine.say(text);print(text)
    engine.runAndWait()
try:
    while True:
        engine.say("Enter the command sir : ");engine.runAndWait();query = input("Enter the command sir : ")
        if query == "stop":
            break
        else:
            result = w.summary(query, sentences=2)
            speak(result)
except:
      speak("Result not found. May be the spelling mistake or unwanted spaces in the command")
