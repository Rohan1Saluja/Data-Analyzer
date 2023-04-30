import pandas as pd
import numpy as np
import pyttsx3 as tts
import speech_recognition as sr

data = pd.read_excel('Book1.xlsx')


class recognize():
    print(data)
    names = data['Name']
    print(names)
    marks = data['Marks']

    def get_name(self, name):
        name.title()
        # print(name)
        for elem in self.names:
            if name == elem:
                # print("inside")
                mark = (data.loc[data['Name'] == name]['Marks'])
                return mark
            # print("inside")
            # mark = (data.loc[data['Name'] == data['Marks']])
            # print(mark)
            # return mark


# obj = recognize()
# marks = obj.get_name('Arjun')
# print(marks)


def JustSpeak(command):
    engine = tts.init()
    engine.say(command)
    engine.runAndWait()


def SpeakText(command):
    readVoice = sr.Recognizer()

    # Initialize the engine
    engine = tts.init()
    engine.say(command)
    engine.runAndWait()
    counter = 0
    print("fine")
    while (counter < 1):
        counter += 1
        # Exception handling to handle
        # exceptions at the runtime
        try:

            with sr.Microphone() as source:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                readVoice.adjust_for_ambient_noise(source, duration=0.2)
                # use the microphone as source for input.
                ask = "Mention Name"
                engine.say(ask)
                engine.runAndWait()
                # listens for the user's input
                audio = readVoice.listen(source)

                # Using google to recognize audio
                MyText = readVoice.recognize_google(audio)
                MyText = MyText.lower()
                print(MyText)

                if MyText == "exit":
                    print("Thank You")
                    JustSpeak("Thank You for Using this Service")
                    break

                confirm = ("Did you say " + MyText)
                JustSpeak(confirm)
                print("Bol ab Yes/No")
                decide = readVoice.listen(source)
                check = readVoice.recognize_google(decide)
                check = check.lower()
                print(check)
                if check == "yes":
                    obj = recognize()
                    marks = obj.get_name(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")


bolBhai = "Hey,How Are you?"
SpeakText(bolBhai)
