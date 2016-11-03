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

#     left_button = ttk.Button(main_frame, text='Left')
#     left_button.grid()
#
#     right_button = ttk.Button(main_frame, text='Right')
#     right_button.grid()
#
#     spin_button = ttk.Button(main_frame, text='Spin')
#     spin_button.grid()

    connect_button = ttk.Button(main_frame, text='Connect')
    connect_button.grid()
    disconnect_button = ttk.Button(main_frame, text='disconnect')
    disconnect_button.grid()

    connect_button['command'] = lambda: connect(dc)
    disconnect_button['command'] = lambda:disconnect(dc)

#     left_button['command'] = lambda: go_left_button()
#     right_button['command'] = lambda: go_right()
#     spin_button['command'] = lambda: spin()


    root.bind_all('<KeyPress>', lambda event: pressed_a_key(event))
    root.bind_all('<KeyRelease>', lambda event: released_a_key(event))


    root.bind_all('<Key-l>', lambda event: go_left(event, dc))
    root.bind_all('<Key-r>', lambda event: go_right(event, dc))
    root.bind_all('<Key-f>', lambda event: go_forward(event, dc))
    root.bind_all('<Key-s>', lambda event: stop(event, dc))
    root.bind_all('<Key-space>', lambda event: spin(event, dc))






def connect(dc):

    dc.robot.connector.connect(4)
    print('robot connected', dc.robot)
def disconnect(dc):

    dc.robot.connector.disconnect()
    print('robot disconnected', dc.robot)

    def pressed_a_key(event):

        print('You pressed the', event.keysym, 'key')


    def released_a_key(event):
        print('You released the', event.keysym, 'key')


    def go_left(event, dc):
        print('You pressed the ' + event.keysym + ' key: ', end='')
        print('Go left!')
        dc.robot.motor_controller.drive_pwm(0, 50)

    def go_forward(entry_box, dc):
#         contents_of_entry_box = entry_box.get()
        dc.robot.motor_controller.drive_pwm(50, 50)


    def go_left_button():
        print('You clicked the Left button: ', end='')
        print('Go left!')


    def go_right(event, dc):
#     if event == None:
#         print('Button press: ', end='')
#     else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
        print('Go right!')
        dc.robot.motor_controller.drive_pwm(50, 0)


    def spin(event, dc):
        dc.robot.motor_controller.drive_pwm(30, 50)

    def stop(event, dc):
        dc.robot.motor_controller.stop()







# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
