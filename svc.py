# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 17:58:40 2023

@author: oguru
"""

import speech_recognition as sr
import pyttsx3

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def perform_calculation(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def respond(text):
    engine.say(text)
    engine.runAndWait()

def main():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio).lower()
            print(f"Command: {command}")
            
            if "calculate" in command:
                expression = command.replace("calculate", "")
                result = perform_calculation(expression)
                respond(f"The result of {expression} is {result}")
            elif "exit" in command:
                respond("Exiting the voice control app.")
                exit()
            else:
                respond("Command not recognized.")
        
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error with the request: {e}")

if __name__ == "__main__":
    respond("Welcome to the voice control app. Please give a command.")
    while True:
        main()
