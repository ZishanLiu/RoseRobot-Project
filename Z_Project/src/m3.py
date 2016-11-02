"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: PUT-YOUR-NAME-HERE.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.


import time
import random
import m0
import tkinter
from tkinter import ttk

def my_frame(root, dc):
    """
    Constructs and returns a   ttk.Frame   on the given root window.
    The frame contains all of this module's widgets.
    Does NOT   grid   the Frame, since the caller will do that.
    Also sets up callbacks for this module's widgets.

    The first argument is the  root  window (a tkinter.Tk object)
    onto which the   ttk.Frame  returned from this function
    will be placed.  The second argument is the shared DataContainer
    object that is CONSTRUCTED in m0 but USED in m1, m2, m3 and m4.

    Preconditions:
      :type root: tkinter.Tk
      :type dc:   m0.DataContainer
    """
    print('Song')
    print()
    N = int(input('N:'))
    Time1 = float(input("Length of Time(min):"))
    Time2 = float(input("Length of Time(max):"))

    frequencies = [262, 294, 330, 349, 392, 440, 494]
    notes = []

    for k in range(N):
        randomnumber = int(random.randrange(7))
        notes = notes + [frequencies[randomnumber]]

    for k in range(N):
        print(notes[k])
        dc.robot.buzzer.play_tone(notes[k])
        Time = Time1 + (Time2 - Time1) * (random.random())
        print(Time)
        time.sleep(Time)
        dc.robot.buzzer.stop()







# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
   m0.main()
