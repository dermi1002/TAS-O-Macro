from pynput import keyboard

def keyboard_listener(userKey):
    def on_press(key):
        if key == keyboard.KeyCode.from_char(userKey):
            print('placeholder frame advance function')

    def on_release(key):
        if key == keyboard.Key.esc:
            print("Quitting...")
            return False

    listener = keyboard.Listener(
        on_press = on_press,
        on_release = on_release
    )

    listener.start()

    print("Keyboard Action started. Press \'Esc\' to quit.")

    listener.join()

def main():
    print('This is a module and is not meant to be executed as a standalone program.')

if __name__ == '__main__':
    main()