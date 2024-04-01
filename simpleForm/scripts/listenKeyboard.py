import keyboard, os

def listenKeyboard():
    if (os.name == "nt"):
        event = keyboard.read_event().name
        [ keyboard.press_and_release('backspace') for i in range(len(event)) ]
        return event
    else:
        pass