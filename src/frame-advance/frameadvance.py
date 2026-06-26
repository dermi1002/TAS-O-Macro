# import keyboard as kb
import xspeedhack as xsh
import time

# variables here

speedhackClient = None

# functions here

def define_process(process, arch):
    speedhackClient = xsh.Client(process, arch=arch)
    return speedhackClient

def wait_one_frame(framerate: int):
    time.sleep( (1 / framerate) )

def stop_time():
    speedhackClient.set_speed(0.0)

def resume_time():
    speedhackClient.set_speed(1.0)

def advance_frame():
    resume_time()
    wait_one_frame()
    stop_time()

def keyboard_action(userKey: str): # will have to separate this into a different script
    while True:
        kb.wait(userKey)
        print('the user defined key is pressed')

# execution

def main():
    print("This file is a module and is not meant to be executed alone.")

if __name__ == '__main__':
    main()