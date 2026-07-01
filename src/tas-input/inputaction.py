import vgamepad as vg

# Gamepad Labels

menuStart = vg.XUSB_BUTTON.XUSB_GAMEPAD_START
menuBack = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK

dpadUp = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
dpadDown = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
dpadLeft = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
dpadRight = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT

faceA = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
faceB = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
faceX = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
faceY = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y

bumperLeft = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
bumperRight = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER

thumbButtonLeft = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
thumbButtonRight = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB

def initialize_gamepad():
    global gamepad
    gamepad = vg.VX360Gamepad()

# Button Functions

def press_button(button):
    gamepad.press_button(button=button)
    gamepad.update()

def release_button(button):
    gamepad.release_button(button=button)
    gamepad.update()

# Joystick & Trigger Functions

def set_left_stick_value(stickValue: float):
    gamepad.left_joystick_float(value=stickValue)
    gamepad.update()

def set_right_stick_value(stickValue: float):
    gamepad.right_joystick_float(value=stickValue)
    gamepad.update()

def set_left_trigger_value(triggerValue: int):
    gamepad.left_trigger(value=triggerValue)
    gamepad.update()

def set_right_trigger_value(triggerValue: int):
    gamepad.right_trigger(value=triggerValue)
    gamepad.update()

def main():
    print("This is a module and is not meant to be executed as a standalone script.")

if __name__ == '__main__':
    main()