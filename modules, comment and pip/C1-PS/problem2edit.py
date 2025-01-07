import pyttsx3

engine = pyttsx3.init()
gender = input("Are you male or female? (m/f): ").strip().lower()

if gender == "m":
    engine.say("What can I do for you, sir?")
elif gender == "f":
    engine.say("What can I do for you, madam?")
else:
    engine.say("What can I do for you?")

engine.runAndWait()