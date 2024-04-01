from pynput import keyboard

class MyListener:
    def __init__(self):
        self.current_key = None
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        self.current_key = key

    def get_key(self):
        return self.current_key

def listenKeyboard():
    listener = MyListener()
    while True:
        if listener.get_key() is not None:
            event = str(listener.get_key())
            listener.current_key = None
            return event

print(listenKeyboard())