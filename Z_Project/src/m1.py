"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: PUT-YOUR-NAME-HERE.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m2
import m3
import m4

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
# import rosebot.faux_rosebot as rb

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
    main_frame.grid(row=1, column=4)


    connect_button = ttk.Button(main_frame, text='Connect')
    connect_button.grid()
    disconnect_button = ttk.Button(main_frame, text='disconnect')
    disconnect_button.grid()

    connect_button['command'] = lambda: connect(dc)
    disconnect_button['command'] = lambda:disconnect(dc)



def connect(dc):
    dc.robot = rb.RoseBot()
    dc.robot.connector.connect(7)
    print('robot connected', dc.robot)
def disconnect(dc):
    dc.robot = rb.RoseBot()
    dc.robot.connector.disconnect()
    print('robot disconnected', dc.robot)


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
