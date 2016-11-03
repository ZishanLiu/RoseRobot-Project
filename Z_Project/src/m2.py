"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: PUT-YOUR-NAME-HERE.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m3
import m4

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
import time

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
    main_frame.grid(row=1, column=2)

    left_button = ttk.Button(main_frame, text='Spin Left')
    left_button['command'] = lambda: turn_left(dc)
    left_button.grid()

    right_button = ttk.Button(main_frame, text='Spin Right')
    right_button['command'] = lambda: turn_right(dc)
    right_button.grid()

    dc.entry_box1 = ttk.Entry(main_frame, text='Speed')
    dc.entry_box1.grid()

    forward_button = ttk.Button(main_frame, text='move forward')
    forward_button['command'] = (lambda: move_forward(dc))
    forward_button.grid()

    backward_button = ttk.Button(main_frame, text='move backward')
    backward_button['command'] = lambda: move_backward(dc)
    backward_button.grid()

    dc.entry_box2 = ttk.Entry(main_frame, text='Distance')
    dc.entry_box2.grid()

    print_entry = ttk.Button(main_frame, text=' Go! ')
    print_entry['command'] = (lambda: move_forward(dc))
    print_entry.grid()

    stop_button = ttk.Button(main_frame, text='stop')
    stop_button['command'] = lambda: stop(dc)
    stop_button.grid()




def move_forward(dc):
    a = dc.entry_box1.get()
    n = int(a)
    dc.robot.motor_controller.drive_pwm(n, n)

def turn_left(dc):
    dc.robot.motor_controller.drive_pwm(0, 100)

def turn_right(dc):
    dc.robot.motor_controller.drive_pwm(100, 0)

def move_backward(dc):
    a = dc.entry_box1.get()
    m = int(a)
    dc.robot.motor_controller.drive_pwm(-m, -m)

def stop(dc):
    dc.robot.motor_controller.drive_pwm(0, 0)


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
