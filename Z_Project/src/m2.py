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
import rosebot.faux_rosebot as rb
import time

def main():
    robot = rb.RoseBot()
    robot.connector.connect(4)

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
    main_frame.grid()

    left_button = ttk.Button(main_frame, text='Spin Left')
    left_button['command'] = lambda: turn_left()
    left_button.grid()

    right_button = ttk.Button(main_frame, text='Spin Right')
    right_button['command'] = lambda: turn_right()
    right_button.grid()

    entry_box = ttk.Entry(main_frame, text='Speed')
    entry_box.grid()

    forward_button = ttk.Button(main_frame, text='move forward')
    forward_button['command'] = lambda: move_forward(entry_box)
    forward_button.grid()

    backward_button = ttk.Button(main_frame, text='move backward')
    backward_button['command'] = lambda: move_backward(entry_box)
    backward_button.grid()

    print_entry = ttk.Button(main_frame, text=' Go! ')
    print_entry['command'] = (lambda: move_forward(entry_box))
    print_entry.grid()


    def move_forward(entry_box):
        contents_of_entry_box = entry_box.get()
        dc.robot.motor_controller.drive_pwm(contents_of_entry_box, contents_of_entry_box)

    def turn_left():
        dc.robot.motor_controller.drive_pwm(0, 100)

    def turn_right():
        dc.robot.motor_controller.drive_pwm(100, 0)

    def move_backward(entry_box):
        contents_of_entry_box = float(entry_box.get())
        dc.robot.motor_controller.drive_pwm(-contents_of_entry_box, -contents_of_entry_box)

    root.mainloop()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
