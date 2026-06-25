FRAME ADVANCE:

use Python.

use xspeedhack library

user defines what key to listen to to implement frame advance.

user defines name of program.

for the time being, framerate is defined by 1 second divided by user-defined framerate number.

PROGRAM:

frame rate function:

if user-defined key is pressed and can frame advance value is true:

set program speed to 1

sleep for user-defined framerate frame

set program speed to 0

set can frame advance value to false

wait key release function

wait key release function:

if user-defined key is released:

set can frame advance value to true
