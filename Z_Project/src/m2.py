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


    main_frame = ttk.Frame(root, padding=50)
    main_frame.grid(row=1, column=2)

    left_button = ttk.Button(main_frame, text='Turn Left')
    left_button['command'] = lambda: turn_left(dc)
    left_button.grid()

    right_button = ttk.Button(main_frame, text='Turn Right')
    right_button['command'] = lambda: turn_right(dc)
    right_button.grid()

    spin_button1 = ttk.Button(main_frame, text='Spin Left')
    spin_button1['command'] = lambda: spin_left(dc)
    spin_button1.grid()

    spin_button2 = ttk.Button(main_frame, text='Spin Right')
    spin_button2['command'] = lambda: spin_right(dc)
    spin_button2.grid()

    label_move = ttk.Label(main_frame)
    label_move['text'] = 'Enter a speed:'
    label_move.grid()

    entry_box1 = ttk.Entry(main_frame, text='Speed')
    entry_box1.grid()

    forward_button = ttk.Button(main_frame, text='move forward')
    forward_button['command'] = lambda: move_forward(dc, entry_box1)
    forward_button.grid()

    entry_box2 = ttk.Entry(main_frame, text='Speed')
    entry_box2.grid()

    backward_button = ttk.Button(main_frame, text='move backward')
    backward_button['command'] = lambda: move_backward(dc, entry_box2)
    backward_button.grid()

    label_speed = ttk.Label(main_frame)
    label_speed['text'] = 'Enter a speed:'
    label_speed.grid()

    entry_box3 = ttk.Entry(main_frame, text='Distance and speed')
    entry_box3.grid()

    label_distance = ttk.Label(main_frame)
    label_distance['text'] = 'Enter a distance:'
    label_distance.grid()

    entry_box4 = ttk.Entry(main_frame, text='Distance')
    entry_box4.grid()

    distance_button = ttk.Button(main_frame, text=' Go! ')
    distance_button['command'] = lambda: distance_go(dc, entry_box3, entry_box4)
    distance_button.grid()

    stop_button = ttk.Button(main_frame, text='stop')
    stop_button['command'] = lambda: stop(dc)
    stop_button.grid()

    label_speed2 = ttk.Label(main_frame)
    label_speed2['text'] = 'Enter a speed:'
    label_speed2.grid()

    entry_box5 = ttk.Entry(main_frame, text='Track')
    entry_box5.grid()

#     label_following = ttk.Label(main_frame)
#     label_following['text'] = 'Enter a distance:'
#     label_following.grid()

    tracking_button = ttk.Button(main_frame, text='Hit wall!')
    tracking_button['command'] = lambda: hit_wall(dc, entry_box5)
    tracking_button.grid()

#     camera_button = ttk.Button(main_frame, text='Camera')
#     camera_button['command'] = lambda: camera(dc)
#     camera_button.grid()

    label_following = ttk.Label(main_frame)
    label_following['text'] = 'Enter a distance:'
    label_following.grid()

    entry_box6 = ttk.Entry(main_frame, text='Track')
    entry_box6.grid()

    label_following_distance = ttk.Label(main_frame)
    label_following_distance['text'] = 'Enter a speed:'
    label_following_distance.grid()

    entry_box7 = ttk.Entry(main_frame, text='Track distance')
    entry_box7.grid()

    follow_button = ttk.Button(main_frame, text='keep distance')
    follow_button['command'] = lambda: keep_distance(dc, entry_box6, entry_box7)
    follow_button.grid()

    main_frame2 = ttk.Frame(root, padding=50)
    main_frame2.grid(row=1, column=5)

    lable1 = ttk.Label(main_frame2)

    lable2 = ttk.Label(main_frame2)

    lable3 = ttk.Label(main_frame2)

    lable4 = ttk.Label(main_frame2)

    lable1.grid()

    lable2.grid()

    lable3.grid()

    lable4.grid()

    time_button = ttk.Button(main_frame2, text='working time')
    time_button['command'] = lambda: working_time(dc, lable1, lable2, lable3, lable4)
    time_button.grid()

def working_time(dc, lable1, lable2, lable3, lable4):
    dc.time_cliked = dc.time_cliked + 1

    if dc.time_cliked % 2 == 1:

        person1 = open('../process/hours-1.txt', 'r').read()
        person2 = open('../process/hours-2.txt', 'r').read()
        person3 = open('../process/hours-3.txt', 'r').read()
        person4 = open('../process/hours-4.txt', 'r').read()

        lable1['text'] = 'Wit Li has worked' + ' ' + str(person1)

        lable2['text'] = 'Zishan Liu has worked' + ' ' + str(person2)

        lable3['text'] = 'Song Luo has worked' + ' ' + str(person3)

        lable4['text'] = 'Ming Lyu has worked' + ' ' + str(person4)

#
#             lable1 = ttk.Label(main_frame2)
#             lable1['text'] = 'Wit Li has worked' + ' ' + str(person1) + ' hours.'
#             lable1.grid()
# #
# #             lable2 = ttk.Label(main_frame2)
# #             lable2['text'] = 'Zishan Liu has worked' + ' ' + str(person2) + ' hours.'
#             lable2.grid()
# #
# #             lable3 = ttk.Label(main_frame2)
# #             lable3['text'] = 'Song Luo has worked' + ' ' + str(person3) + ' hours.'
#             lable3.grid()
# #
# #             lable4 = ttk.Label(main_frame2)
# #             lable4['text'] = 'Ming Lyu has worked' + ' ' + str(person4) + ' hours.'
#             lable4.grid()


    elif dc.time_cliked % 2 == 0 :

        lable1['text'] = ' '


        lable2['text'] = ' '


        lable3['text'] = ' '


        lable4['text'] = ' '


def spin_left(dc):
    dc.robot.motor_controller.drive_pwm(-150, 150)
    print('It is spinning!')

def spin_right(dc):
    dc.robot.motor_controller.drive_pwm(150, -150)
    print('It is spinning!')

def move_forward(dc, entry_box1):
    a = int(entry_box1.get())
    dc.robot.motor_controller.drive_pwm(a, a)

def turn_left(dc):
    dc.robot.motor_controller.drive_pwm(0, 100)
    time.sleep(0.8)
    dc.robot.motor_controller.drive_pwm(0, 0)

def turn_right(dc):
    dc.robot.motor_controller.drive_pwm(100, 0)
    time.sleep(1)
    dc.robot.motor_controller.drive_pwm(0, 0)

def move_backward(dc, entry_box2):
    a = int(entry_box2.get())
    dc.robot.motor_controller.drive_pwm(-a, -a)
    print('It is moving backward')

def stop(dc):
    dc.robot.motor_controller.drive_pwm(0, 0)
    print('Stop!')

def distance_go(dc, entry_box3, entry_box4):

    d = 9 * int(entry_box3.get())
    c = 9 * int(entry_box4.get())

    dc.robot.motor_controller.drive_pwm(d, d)
    time.sleep(c / d)

    dc.robot.motor_controller.drive_pwm(0, 0)

def hit_wall(dc, entry_box5):

    s1 = int(entry_box5.get())
    s2 = 0

    while True:
        dc.robot.motor_controller.drive_pwm(s1, s1)

        if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
            s2 = 1
            break

        elif dc.robot.sensor_reader.right_bump_sensor.read() == 0:
            s2 = 2
            break

    if s2 == 1:
        dc.robot.motor_controller.drive_pwm(-50, 0)
        time.sleep(0.01)

        while True:
            dc.robot.motor_controller.drive_pwm(0, s1)

            if dc.robot.sensor_reader.right_bump_sensor.read() == 0:
#                 dc.robot.motor_controller.drive_pwm(s1, 0)
                break
        dc.robot.motor_controller.drive_pwm(0, -s1)
        time.sleep(0.1)

#                 if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
#                     dc.robot.motor_controller.drive_pwm(0, 0)
#                     break

    if s2 == 2:
        dc.robot.motor_controller.drive_pwm(0, -50)
        time.sleep(0.01)

        while True:
            dc.robot.motor_controller.drive_pwm(s1, 0)

            if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
#                 dc.robot.motor_controller.drive_pwm(0, s1)
                break

        dc.robot.motor_controller.drive_pwm(-s1, 0)
        time.sleep(0.1)

#                 if dc.robot.sensor_reader.right_bump_sensor.read() == 0:
#                     dc.robot.motor_controller.drive_pwm(0, 0)
#                     break

    dc.robot.motor_controller.drive_pwm(0, 0)

def keep_distance(dc, entry_box6, entry_box7):

    print('The middle proximity sensor is on!')

    speed = int(entry_box7.get())

    distance = int(entry_box6.get())

    while True:
        dc.robot.motor_controller.drive_pwm(speed, speed)

        if dc.robot.sensor_reader.front_proximity_sensor.read() > distance:
            dc.robot.motor_controller.drive_pwm(-speed, -speed)

        if dc.robot.sensor_reader.front_proximity_sensor.read() < distance:
            dc.robot.motor_controller.drive_pwm(speed, speed)

        if dc.robot.sensor_reader.front_proximity_sensor.read() == distance:
            dc.robot.motor_controller.drive_pwm(0, 0)

        if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break

        if dc.robot.sensor_reader.right_bump_sensor.read() == 0:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break

    dc.robot.motor_controller.drive_pwm(0, 0)



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
