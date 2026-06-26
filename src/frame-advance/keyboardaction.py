from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def keyboard_listener():
    listener = keyboard.Listener(
        on_press = on_press,
        on_release = on_release
    )
    listener.start()
    print("Keyboard Action started. Press \'Esc\' to quit.")
    listener.join()

def main():
    keyboard_listener()

if __name__ == '__main__':
    main()