import xspeedhack as xsh
import time

# variables here

speedhackClient = None

canSpeedhack: bool = True

# functions here

def check_speedhack_condition():
    print("Is speedhack on:", canSpeedhack, '\n')

def enable_speedhack():
    global canSpeedhack
    canSpeedhack = True
    check_speedhack_condition()

def disable_speedhack():
    global canSpeedhack
    canSpeedhack = False
    check_speedhack_condition()

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
    if canSpeedhack:
        resume_time()
        wait_one_frame()
        stop_time()
        disable_speedhack()

# execution

def main():
    print("This file is a module and is not meant to be executed alone.")

if __name__ == '__main__':
    main()