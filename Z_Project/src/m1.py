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
import rosebot.faux_rosebot as rb
import time
# import rosebot.faux_rosebot as rb
# points = '(10,11),(20,21),(30,31)'
# point2 = points.replace('(', '').replace(')', '').split(',')
# print(point2)






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

    dc.connect_entry = ttk.Entry(main_frame)
    dc.connect_entry.grid()
    connect_button['command'] = lambda: connect(dc)
    disconnect_button['command'] = lambda:disconnect(dc)

#     left_button['command'] = lambda: go_left_button()
#     right_button['command'] = lambda: go_right()
#     spin_button['command'] = lambda: spin()


#     root.bind_all('<KeyPress>', lambda event: pressed_a_key(event))
#     root.bind_all('<KeyRelease>', lambda event: released_a_key(event))
    slow_speed_button = ttk.Button(main_frame, text='slow_speed')
    slow_speed_button['command'] = lambda: slow_mode(root, dc)
    slow_speed_button.grid()
    medium_speed_button = ttk.Button(main_frame, text='medium_speed')
    medium_speed_button['command'] = lambda: medium_mode(root, dc)
    medium_speed_button.grid()
    fast_speed_button = ttk.Button(main_frame, text='fast_speed')
    fast_speed_button['command'] = lambda: fast_mode(root, dc)
    fast_speed_button.grid()
#     root.bind_all('<Key-a>', lambda event: go_left(event, dc))
#     root.bind_all('<Key-d>', lambda event: go_right(event, dc))
#     root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
#     root.bind_all('<Key-s>', lambda event: go_backward(event, dc))
#     root.bind_all('<Key-p>', lambda event: stop(event, dc))
#     root.bind_all('<Key-space>', lambda event: spin(event, dc))


    waypoints_button = ttk.Button(main_frame, text='waypoints')
    waypoints_button['command'] = lambda: move_waypoints(dc)
    waypoints_button.grid()
    dc.my_entry = ttk.Entry(main_frame)
    dc.my_entry.grid()
    dc.points_entry = ttk.Entry(main_frame)
    dc.points_entry.grid()


    wireless_connect_button = ttk.Button(main_frame, text='wireless connect')
    wireless_connect_button.grid()
    wireless_connect_button['command'] = lambda: wireless_connect(dc)







def wireless_connect(dc):
    a = dc.connect_entry.get()
    dc.robot.connector.connect_wireless(a)
    print('robot wireless connected', dc.robot)
def connect(dc):

    dc.robot.connector.connect(8)
    print('robot connected', dc.robot)
def disconnect(dc):

    dc.robot.connector.disconnect()
    print('robot disconnected', dc.robot)

# def pressed_a_key(event):
#
#     print('You pressed the', event.keysym, 'key')
#
#
# def released_a_key(event):
#     print('You released the', event.keysym, 'key')
def slow_mode(root, dc):
    speed = 20
    root.bind_all('<Key-a>', lambda event: go_left(event, dc))
    root.bind_all('<Key-d>', lambda event: go_right(event, dc))
    root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
    root.bind_all('<Key-s>', lambda event: go_backward(event, dc))
    root.bind_all('<Key-p>', lambda event: stop(event, dc))
    root.bind_all('<Key-space>', lambda event: spin(event, dc))
    def go_left(event, dc):
        print('You pressed the ' + event.keysym + ' key: ', end='')
        dc.robot.motor_controller.drive_pwm(0, speed)

    def go_forward(event, dc):
        dc.robot.motor_controller.drive_pwm(speed, speed)


    def go_left_button():
        print('You clicked the Left button: ', end='')


    def go_right(event, dc):
#     if event == None:
#         print('Button press: ', end='')
#     else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
        dc.robot.motor_controller.drive_pwm(speed, 0)


    def spin(event, dc):
        dc.robot.motor_controller.drive_pwm(10, speed)
    def go_backward(event, dc):
        dc.robot.motor_controller.drive_pwm(-(speed), -(speed))

    def stop(event, dc):
        dc.robot.motor_controller.stop()
def medium_mode(root, dc):
    speed = 30
    root.bind_all('<Key-a>', lambda event: go_left(event, dc))
    root.bind_all('<Key-d>', lambda event: go_right(event, dc))
    root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
    root.bind_all('<Key-s>', lambda event: go_backward(event, dc))
    root.bind_all('<Key-p>', lambda event: stop(event, dc))
    root.bind_all('<Key-space>', lambda event: spin(event, dc))
    def go_left(event, dc):
        print('You pressed the ' + event.keysym + ' key: ', end='')
        print('Go left!')
        dc.robot.motor_controller.drive_pwm(0, speed)

    def go_forward(event, dc):
        dc.robot.motor_controller.drive_pwm(speed, speed)


    def go_left_button():
        print('You clicked the Left button: ', end='')
        print('Go left!')


    def go_right(event, dc):
        print('You pressed the ' + event.keysym + ' key: ', end='')
        print('Go right!')
        dc.robot.motor_controller.drive_pwm(speed, 0)


    def spin(event, dc):
        dc.robot.motor_controller.drive_pwm(10, speed)
    def go_backward(event, dc):
        dc.robot.motor_controller.drive_pwm(-(speed), -(speed))

    def stop(event, dc):
        dc.robot.motor_controller.stop()

def fast_mode(root, dc):
    speed = 40
    root.bind_all('<Key-a>', lambda event: go_left(event, dc))
    root.bind_all('<Key-d>', lambda event: go_right(event, dc))
    root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
    root.bind_all('<Key-s>', lambda event: go_backward(event, dc))
    root.bind_all('<Key-p>', lambda event: stop(event, dc))
    root.bind_all('<Key-space>', lambda event: spin(event, dc))
    def go_left(event, dc):
        print('You pressed the ' + event.keysym + ' key: ', end='')
        print('Go left!')
        dc.robot.motor_controller.drive_pwm(0, speed)

    def go_forward(event, dc):
        dc.robot.motor_controller.drive_pwm(speed, speed)


    def go_right(event, dc):
#     if event == None:
#         print('Button press: ', end='')
#     else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
        print('Go right!')
        dc.robot.motor_controller.drive_pwm(speed, 0)


    def spin(event, dc):
        dc.robot.motor_controller.drive_pwm(10, speed)
    def go_backward(event, dc):
        dc.robot.motor_controller.drive_pwm(-(speed), -(speed))

    def stop(event, dc):
        dc.robot.motor_controller.stop()

# def go_left(event, dc):
#     print('You pressed the ' + event.keysym + ' key: ', end='')
#     print('Go left!')
#     dc.robot.motor_controller.drive_pwm(speed, speed)
#
# def go_forward(entry_box, dc):
#     dc.robot.motor_controller.drive_pwm(50, 50)
#
#
# def go_left_button():
#     print('You clicked the Left button: ', end='')
#     print('Go left!')
#
#
# def go_right(event, dc):
# #     if event == None:
# #         print('Button press: ', end='')
# #     else:
#     print('You pressed the ' + event.keysym + ' key: ', end='')
#     print('Go right!')
#     dc.robot.motor_controller.drive_pwm(50, 0)
#
#
# def spin(event, dc):
#     dc.robot.motor_controller.drive_pwm(30, 50)
# def go_backward(event, dc):
#     dc.robot.motor_controller.drive_pwm(-40, -40)
#
# def stop(event, dc):
#     dc.robot.motor_controller.stop()
def move_waypoints(dc):
    a = dc.my_entry.get()
    speed = int(a)
#     dc.robot.motor_controller.drive_pwm(speed, speed)
#     dc.robot.motor_controller.drive_pwm(speed, speed)
    content1 = dc.points_entry.get()
    points_fake = str(content1)
    points = points_fake.replace('(', '').replace(')', '').split(',')

    times = (15.7 / speed)
    for k in range(len(points)):
        if k % 2 == 0:
            timex = int(points[k]) / speed
            dc.robot.motor_controller.drive_pwm(speed, 0)
            time.sleep(times)
            dc.robot.motor_controller.drive_pwm(speed, speed)
            time.sleep(timex)
        if k % 2 != 0:
            timey = int(points[k]) / speed
            dc.robot.motor_controller.drive_pwm(0, speed)
            time.sleep(times)
            dc.robot.motor_controller.drive_pwm(speed, speed)
            time.sleep(timey)










# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
