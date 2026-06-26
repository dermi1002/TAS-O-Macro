import keyboard as kb
import xspeedhack as xsh

import time

# variables here

speedhackClient = None

# functions here

def define_process(process, arch):
    speedhackClient = xsh.Client(process, arch=arch)
    return speedhackClient

def wait_one_frame():
    time.sleep(1)

def stop_time():
    speedhackClient.set_speed(0.0)

def resume_time():
    speedhackClient.set_speed(1.0)

def advance_frame():
    resume_time()
    wait_one_frame()
    stop_time()


# execution

def main():
    pass

if __name__ == '__main__':
    main()