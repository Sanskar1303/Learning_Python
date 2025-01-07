import pyttsx3

engine = pyttsx3.init()
gender = input("Are you male or female? (male/female): ").strip().lower()

if gender == "male":
    engine.say("What can I do for you, sir?")
elif gender == "female":
    engine.say("What can I do for you, madam?")
else:
    engine.say("What can I do for you?")

engine.runAndWait()