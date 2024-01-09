"""
Project: SimpleForm
Author: Alan Reis Anjos
License: Creative Commons Attribution 4.0 International License
License Details: https://creativecommons.org/licenses/by/4.0/
"""

import keyboard

def listenKeyboard():
    event = keyboard.read_event().name
    [ keyboard.press_and_release('backspace') for i in range(100) ]
    return event