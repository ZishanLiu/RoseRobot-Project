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


    dc.entry_box1 = ttk.Entry(main_frame, text='Number of Notes')
    dc.entry_box1.grid()
    dc.entry_box2 = ttk.Entry(main_frame, text='length of Time')
    dc.entry_box2.grid()
    button1 = ttk.Button(main_frame, text='Make Sound')
    button1['command'] = lambda: songs_playing(dc)
    button1.grid()



    button2 = ttk.Button(main_frame, text='Compose Music and dance with light on')
    button2['command'] = lambda: songs_composing(dc)
    button2.grid()








def songs_playing(dc):

    notes = []
    N = int(dc.entry_box1.get())
    Time1 = int(dc.entry_box2.get())
    Time2 = Time1

    for k in range(N):
        randomnumber = int(random.randrange(1, 120))
        notes = notes + [randomnumber] + [999999]
    for k in range(N * 2):
        if notes[k] != 999999:
            print(notes[k])
            dc.robot.buzzer.play_tone(notes[k])
            Time = Time1 + (Time2 - Time1) * (random.random())
            print(Time)
            time.sleep(Time)
        else:
            dc.robot.buzzer.play_tone(0)
            time.sleep(0.01)

        dc.robot.buzzer.stop()


def songs_composing(dc):
    k = random.randrange(0, 2)
    ryhme1 = ([0.5, 0.25, 0.25, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5], [0.5, 0.25, 0.25, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5])
    ryhme2 = [(0.5, 0.5, 0.5, 0.5, 0.5, 0.5), (0.5, 0.5, 0.5, 0.5, 0.5, 1)]
    ryhme3 = [(0.5, 0.5, 1, 0.5, 1, 1), (3, 1, 1, 0.5, 1, 1)]
    list1 = (58, 55, 21, 50, 19, 28, 15, 59, 56, 58, 21, 24, 19)
    list2 = (28, 27, 55, 56, 60, 61, 49, 37, 36, 33, 33, 30)
    list3 = ()
    for a in range(len(ryhme1[random.randrange(0, 2)])):

        dc.robot.buzzer.play_tone(random.choice(list1))
        dc.robot.motor_controller.drive_pwm(random.randrange(-100, 100), random.randrange(-100, 100))
        time.sleep(ryhme1[k][a % len(ryhme1[k])])
        dc.robot.buzzer.stop()
        dc.robot.led.turn_on()
    dc.robot.motor_controller.drive_pwm(0, 0)
    dc.robot.led.turn_off()






# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
   m0.main()
