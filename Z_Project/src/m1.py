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


    connect_button['command'] = lambda: connect(dc)
    disconnect_button['command'] = lambda:disconnect(dc)

#     left_button['command'] = lambda: go_left_button()
#     right_button['command'] = lambda: go_right()
#     spin_button['command'] = lambda: spin()


#     root.bind_all('<KeyPress>', lambda event: pressed_a_key(event))
#     root.bind_all('<KeyRelease>', lambda event: released_a_key(event))
    slow_speed_button = ttk.Radiobutton(main_frame, text='slow_speed', value='slow')
    slow_speed_button['command'] = lambda: slow_mode(root, dc)
    slow_speed_button.grid()
    medium_speed_button = ttk.Radiobutton(main_frame, text='medium_speed', value='medium')
    medium_speed_button['command'] = lambda: medium_mode(root, dc)
    medium_speed_button.grid()
    fast_speed_button = ttk.Radiobutton(main_frame, text='fast_speed', value='fast')
    fast_speed_button['command'] = lambda: fast_mode(root, dc)
    fast_speed_button.grid()
    sound_mode_button = ttk.Button(main_frame, text='sound mode')
    sound_mode_button['command'] = lambda: sound(root, dc)
    sound_mode_button.grid()
#     root.bind_all('<Key-a>', lambda event: go_left(event, dc))
#     root.bind_all('<Key-d>', lambda event: go_right(event, dc))
#     root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
#     root.bind_all('<Key-s>', lambda event: go_backward(event, dc))
#     root.bind_all('<Key-p>', lambda event: stop(event, dc))
#     root.bind_all('<Key-space>', lambda event: spin(event, dc))


    waypoints_button = ttk.Button(main_frame, text='waypoints')
    waypoints_button['command'] = lambda: move_waypoints(dc)
    waypoints_button.grid()
    goback_button = ttk.Button(main_frame, text='goback')
    goback_button['command'] = lambda: goback(dc)
    goback_button.grid()
    label1 = ttk.Label(main_frame, text='Speed for wayoints')
    label1.grid()
    dc.my_entry = ttk.Entry(main_frame)
    dc.my_entry.grid()
    label2 = ttk.Label(main_frame, text='coordinates for waypoints')
    label2.grid()
    dc.points_entry = ttk.Entry(main_frame)
    dc.points_entry.grid()

    label3 = ttk.Label(main_frame, text='port for connection')
    label3.grid()
    dc.connect_entry = ttk.Entry(main_frame)
    dc.connect_entry.grid()
    wireless_connect_button = ttk.Button(main_frame, text='wireless connect')
    wireless_connect_button.grid()
    wireless_connect_button['command'] = lambda: wireless_connect(dc)







def wireless_connect(dc):
    a = dc.connect_entry.get()
    dc.robot.connector.connect_wireless(a)
    print('robot wireless connected', dc.robot)
def connect(dc):

    dc.robot.connector.connect(10)
    print('robot connected', dc.robot)
def disconnect(dc):

    dc.robot.connector.disconnect()
    print('robot disconnected', dc.robot)

# def pressed_a_key(event):
#
#     print('You pressed the', event.keysym, 'key')
#
#

def slow_mode(root, dc):
    speed = 40
    root.bind_all('<Key-a>', lambda event: go_left(event, dc))
    root.bind_all('<Key-d>', lambda event: go_right(event, dc))
    root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
    root.bind_all('<Key-s>', lambda event: go_backward(event, dc))
    root.bind_all('<Key-p>', lambda event: stop(event, dc))
    root.bind_all('<Key-space>', lambda event: spin(event, dc))
    root.bind_all('<KeyRelease>', lambda event: release_a_key(dc))
    def release_a_key(dc):
        dc.robot.motor_controller.drive_pwm(0, 0)
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
    speed = 60
    root.bind_all('<Key-a>', lambda event: go_left(event, dc))
    root.bind_all('<Key-d>', lambda event: go_right(event, dc))
    root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
    root.bind_all('<Key-s>', lambda event: go_backward(event, dc))
    root.bind_all('<Key-p>', lambda event: stop(event, dc))
    root.bind_all('<Key-space>', lambda event: spin(event, dc))
    root.bind_all('<KeyRelease>', lambda event: release_a_key(dc))
    def release_a_key(dc):
        dc.robot.motor_controller.drive_pwm(0, 0)
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
    speed = 80
    root.bind_all('<Key-a>', lambda event: go_left(event, dc))
    root.bind_all('<Key-d>', lambda event: go_right(event, dc))
    root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
    root.bind_all('<Key-s>', lambda event: go_backward(event, dc))
    root.bind_all('<Key-p>', lambda event: stop(event, dc))
    root.bind_all('<Key-space>', lambda event: spin(event, dc))
    root.bind_all('<KeyRelease>', lambda event: release_a_key(dc))
    def release_a_key(dc):
        dc.robot.motor_controller.drive_pwm(0, 0)
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
def sound(root, dc):
#     root.bind_all('<Key>')
    root.bind_all('<Key-q>', lambda event:do(dc))
    def do(dc):
        dc.robot.buzzer.play_tone(43)
    root.bind_all('<KeyRelease-q>', lambda event: released_a_keyq(dc))
    def released_a_keyq(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-w>', lambda event:re(dc))
    def re(dc):
        dc.robot.buzzer.play_tone(45)
    root.bind_all('<KeyRelease-w>', lambda event: released_a_keyw(dc))
    def released_a_keyw(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-e>', lambda event:mi(dc))
    def mi(dc):
        dc.robot.buzzer.play_tone(47)
    root.bind_all('<KeyRelease-e>', lambda event: released_a_keye(dc))
    def released_a_keye(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-r>', lambda event:fa(dc))
    def fa(dc):
        dc.robot.buzzer.play_tone(48)
        root.bind_all('<KeyRelease-r>', lambda event: released_a_keyr(dc))
    def released_a_keyr(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-t>', lambda event:so(dc))
    def so(dc):
        dc.robot.buzzer.play_tone(50)
        root.bind_all('<KeyRelease-t>', lambda event: released_a_keyt(dc))
    def released_a_keyt(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-y>', lambda event:la(dc))
    def la(dc):
        dc.robot.buzzer.play_tone(52)
        root.bind_all('<KeyRelease-y>', lambda event: released_a_keyy(dc))
    def released_a_keyy(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-u>', lambda event:si(dc))
    def si(dc):
        dc.robot.buzzer.play_tone(54)
        root.bind_all('<KeyRelease-u>', lambda event: released_a_keyu(dc))
    def released_a_keyu(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-i>', lambda event: h_do(dc))
    def h_do(dc):
        dc.robot.buzzer.play_tone(55)
        root.bind_all('<KeyRelease-i>', lambda event: released_a_keyi(dc))
    def released_a_keyi(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-o>', lambda event: h_re(dc))
    def h_re(dc):
        dc.robot.buzzer.play_tone(57)
        root.bind_all('<KeyRelease-o>', lambda event: released_a_keyo(dc))
    def released_a_keyo(dc):
        dc.robot.buzzer.stop()

    root.bind_all('<Key-p>', lambda event: h_mi(dc))
    def h_mi(dc):
        dc.robot.buzzer.play_tone(59)
        root.bind_all('<KeyRelease-p>', lambda event: released_a_keyp(dc))
    def released_a_keyp(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-a>', lambda event:h_fa(dc))
    def h_fa(dc):
        dc.robot.buzzer.play_tone(60)
        root.bind_all('<KeyRelease-a>', lambda event: release_a_keya(dc))
    def release_a_keya(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-s>', lambda event:h_so(dc))
    def h_so(dc):
        dc.robot.buzzer.play_tone(62)
        root.bind_all('<KeyRelease-s>', lambda event: release_a_keys(dc))
    def release_a_keys(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-d>', lambda event:h_la(dc))
    def h_la(dc):
        dc.robot.buzzer.play_tone(64)
        root.bind_all('<KeyRelease-d>', lambda event: release_a_keyd(dc))
    def release_a_keyd(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-f>', lambda event:h_si(dc))
    def h_si(dc):
        dc.robot.buzzer.play_tone(66)
        root.bind_all('<KeyRelease-f>', lambda event: release_a_keyf(dc))
    def release_a_keyf(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-g>', lambda event:hh_do(dc))
    def hh_do(dc):
        dc.robot.buzzer.play_tone(67)
        root.bind_all('<KeyRelease-g>', lambda event: release_a_keyg(dc))
    def release_a_keyg(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-h>', lambda event:hh_re(dc))
    def hh_re(dc):
        dc.robot.buzzer.play_tone(69)
        root.bind_all('<KeyRelease-h>', lambda event: release_a_keyh(dc))
    def release_a_keyh(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-j>', lambda event:hh_mi(dc))
    def hh_mi(dc):
        dc.robot.buzzer.play_tone(71)
        root.bind_all('<KeyRelease-j>', lambda event: release_a_keyj(dc))
    def release_a_keyj(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-k>', lambda event:hh_fa(dc))
    def hh_fa(dc):
        dc.robot.buzzer.play_tone(72)
        root.bind_all('<KeyRelease-k>', lambda event: release_a_keyk(dc))
    def release_a_keyk(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-l>', lambda event:hh_so(dc))
    def hh_so(dc):
        dc.robot.buzzer.play_tone(74)
        root.bind_all('<KeyRelease-l>', lambda event: release_a_keyl(dc))
    def release_a_keyl(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-z>', lambda event: l_si(dc))
    def l_si(dc):
        dc.robot.buzzer.play_tone(42)
        root.bind_all('<KeyRelease-z>', lambda event:release_a_keyz(dc))
    def release_a_keyz(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-x>', lambda event: l_la(dc))
    def l_la(dc):
        dc.robot.buzzer.play_tone(40)
        root.bind_all('<KeyRelease-x>', lambda event:release_a_keyx(dc))
    def release_a_keyx(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-c>', lambda event: l_so(dc))
    def l_so(dc):
        dc.robot.buzzer.play_tone(38)
        root.bind_all('<KeyRelease-c>', lambda event:release_a_keyc(dc))
    def release_a_keyc(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-v>', lambda event: l_fa(dc))
    def l_fa(dc):
        dc.robot.buzzer.play_tone(36)
        root.bind_all('<KeyRelease-v>', lambda event:release_a_keyv(dc))
    def release_a_keyv(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-b>', lambda event: l_mi(dc))
    def l_mi(dc):
        dc.robot.buzzer.play_tone(35)
        root.bind_all('<KeyRelease-b>', lambda event:release_a_keyb(dc))
    def release_a_keyb(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-n>', lambda event: l_re(dc))
    def l_re(dc):
        dc.robot.buzzer.play_tone(33)
        root.bind_all('<KeyRelease-n>', lambda event:release_a_keyn(dc))
    def release_a_keyn(dc):
        dc.robot.buzzer.stop()
    root.bind_all('<Key-m>', lambda event: l_do(dc))
    def l_do(dc):
        dc.robot.buzzer.play_tone(31)
        root.bind_all('<KeyRelease-m>', lambda event:release_a_keym(dc))
    def release_a_keym(dc):
        dc.robot.buzzer.stop()

def move_waypoints(dc):
    a = dc.my_entry.get()
    speed = int(a)
#     dc.robot.motor_controller.drive_pwm(speed, speed)
#     dc.robot.motor_controller.drive_pwm(speed, speed)
    content1 = dc.points_entry.get()
    points_fake = str(content1)
    points = points_fake.replace('(', '').replace(')', '').split(',')

    times = (110 / speed)
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
    dc.robot.motor_controller.drive_pwm(0, 0)
def goback(dc):
    a = dc.my_entry.get()
    speed = int(a)
    content1 = dc.points_entry.get()
    points_fake = str(content1)
    points = points_fake.replace('(', '').replace(')', '').split(',')
    times = (110 / speed)
    timea = (200 / speed)
    dc.robot.motor_controller.drive_pwm(speed, 0)
    time.sleep(timea)
    for k in range(len(points)):
        if k % 2 == 0:
            timex = int(points[k]) / speed
#             dc.robot.motor_controller.drive_pwm(speed, 0)
#             time.sleep(times)
            dc.robot.motor_controller.drive_pwm(speed, speed)
            time.sleep(timex)
        if k % 2 != 0:
            timey = int(points[k]) / speed
            dc.robot.motor_controller.drive_pwm(speed, 0)
            time.sleep(times)
            dc.robot.motor_controller.drive_pwm(speed, speed)
            time.sleep(timey)
    dc.robot.motor_controller.drive_pwm(0, 0)














# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
