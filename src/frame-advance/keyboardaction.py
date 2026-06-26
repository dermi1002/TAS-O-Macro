from pynput import keyboard

def call_frame_advance(userKey: str):
    if key == keyboard.KeyCode.from_char(userKey):
        print('placeholder frame advance function')

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

    call_frame_advance

def on_release(key):
    print( '{0} released'.format(key) )

    if key == keyboard.Key.esc:
        # Stop listener
        return False

def keyboard_listener(userKey):
    userKey = userKey

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