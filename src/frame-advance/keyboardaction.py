from pynput import keyboard

def call_frame_advance(userKey: str): # i might have to move all this to the cli. wish i didn't tho.
    print("aaa")
    def on_press(key):
        if key == keyboard.KeyCode.from_char(userKey):
            print('placeholder frame advance function')

def on_release(key):
    if key == keyboard.Key.esc:
        print("Quitting...")
        return False

def keyboard_listener(userKey):
    listener = keyboard.Listener(
        on_press = call_frame_advance(userKey),
        on_release = on_release
    )

    listener.start()

    print("Keyboard Action started. Press \'Esc\' to quit.")

    listener.join()

def main():
    print('This is a module and is not meant to be executed as a standalone program.')

if __name__ == '__main__':
    main()