import xspeedhack as xsh
import time

# variables here

speedhackClient = None

canSpeedhack: bool = True

# functions here

def check_speedhack_condition():
    print("Is speedhack on:", canSpeedhack, '\n')

def change_speedhack_condition(state: bool):
    global canSpeedhack
    canSpeedhack = state
    check_speedhack_condition()


def define_process(process, arch):
    global speedhackClient
    speedhackClient = xsh.Client(process, arch=arch)
    return speedhackClient

def placeholder_define_process(process, arch):
    print("Process", process, f"({arch})", "started.")

def wait_one_frame(framerate: int):
    time.sleep( (1 / framerate) )

def stop_time():
    speedhackClient.set_speed(0.0)

def resume_time():
    speedhackClient.set_speed(1.0)


def placeholder_frameadvance():
    if canSpeedhack:
        print('placeholder frame advance function')
        change_speedhack_condition(False) # disable speedhack

def advance_frame(framerate):
    if canSpeedhack:
        resume_time()
        wait_one_frame(framerate)
        stop_time()
        change_speedhack_condition(False) # disable speedhack

# execution

def main():
    print("This file is a module and is not meant to be executed alone.")

if __name__ == '__main__':
    main()