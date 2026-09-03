import pyttsx3

voz = pyttsx3.init()

vozes = voz.getProperty("voices")
voz.setProperty("voice", vozes[0].id)

voz.say("Bom dia. Sou o JARVIS. Como posso ajudar?")
voz.runAndWait()
voz.stop()