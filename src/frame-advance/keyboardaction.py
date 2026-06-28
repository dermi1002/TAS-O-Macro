from pynput import keyboard
import frameadvance

def keyboard_listener(userKey, framerate):
    def on_press(key):
        if key == keyboard.KeyCode.from_char(userKey):
            # frameadvance.placeholder_frameadvance()
            frameadvance.advance_frame(framerate)

    def on_release(key):
        if key == keyboard.KeyCode.from_char(userKey):
            frameadvance.change_speedhack_condition(True) # enable speedhack

        if key == keyboard.Key.esc:
            print("Quitting...")
            frameadvance.resume_time
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