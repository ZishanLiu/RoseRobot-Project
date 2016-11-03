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
    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid(row=1, column=0)
    print('Song')
    print()
    dc.entry_box1 = ttk.Entry(main_frame, text='Number of Notes')
    dc.entry_box1.grid()
    dc.entry_box2 = ttk.Entry(main_frame, text='length of Time')
    dc.entry_box2.grid()
    button1 = ttk.Button(main_frame, text='Make Sound')
    button1['command'] = lambda: songs_playing(dc)
    button1.grid()

def songs_playing(dc):

    notes = []
    N = int(dc.entry_box1.get())
    Time1 = int(dc.entry_box2.get())
    Time2 = Time1

    for k in range(N):
        randomnumber = int(random.randrange(256))
        notes = notes + [randomnumber]
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
