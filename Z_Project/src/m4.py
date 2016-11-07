"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: lyum.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m2
import m3

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
    frame = ttk.Frame(root, padding=10)
    frame.grid()

    speedbutton = ttk.Button(frame, text='speed')
    speedbutton['command'] = (lambda:speed(dc))

    dc.speedentry = ttk.Entry(frame)
    dc.darkness = ttk.Entry(frame)
    dc.distanceleft = ttk.Entry(frame)
    dc.distanceright = ttk.Entry(frame)
    dc.distancemiddle = ttk.Entry(frame)
    dc.threshholdentry = ttk.Entry(frame)
    dc.errorentry = ttk.Entry(frame)


    bumpleftbutton = ttk.Button(frame, text='bumpleft')
    bumpleftbutton['command'] = (lambda:bumpleft(dc))
    bumprightbutton = ttk.Button(frame, text='bumpright')
    bumprightbutton['command'] = (lambda:bumpright(dc))
    bumpbothbutton = ttk.Button(frame, text='bumpboth')
    bumpbothbutton['command'] = (lambda:bumpboth(dc))
    reflectanceleftbutton = ttk.Button(frame, text='reflectanceleft')
    reflectanceleftbutton['command'] = (lambda:reflectanceleft(dc))
    reflectancerightbutton = ttk.Button(frame, text='reflectanceright')
    reflectancerightbutton['command'] = (lambda:reflectanceright(dc))
    reflectancemiddlebutton = ttk.Button(frame, text='reflectancemiddle')
    reflectancemiddlebutton['command'] = (lambda:reflectancemiddle(dc))
    proximityleftbutton = ttk.Button(frame, text='proximityleft')
    proximityleftbutton['command'] = (lambda:proximityleft(dc))
    proximityrightbutton = ttk.Button(frame, text='proximityright')
    proximityrightbutton['command'] = (lambda:proximityright(dc))
    proximitymiddlebutton = ttk.Button(frame, text='proximitymiddle')
    proximitymiddlebutton['command'] = (lambda:proximitymiddle(dc))
    BangBangleftbutton = ttk.Button(frame, text='BangBang')
    BangBangleftbutton['command'] = (lambda:BangBangleft(dc))
    dc.threshholdentry = ttk.Entry(frame)
    dc.errorentry = ttk.Entry(frame)


    speedbutton.grid()
    dc.speedentry.grid()
    bumpbothbutton.grid()
    bumpleftbutton.grid()
    bumprightbutton.grid()
    dc.darkness.grid()
    reflectanceleftbutton.grid()
    reflectancemiddlebutton.grid()
    reflectancerightbutton.grid()
    dc.distanceleft.grid()
    proximityleftbutton.grid()
    dc.distanceright.grid()
    proximityrightbutton.grid()
    dc.distancemiddle.grid()
    proximitymiddlebutton.grid()
    dc.threshholdentry.grid()
    dc.errorentry.grid()
    BangBangleftbutton.grid()


def speed(dc):
    myentry = dc.speedentry.get()
    speed = int(myentry)
    dc.robot.motor_controller.drive_pwm(speed, speed)

def bumpleft(dc):
    print(dc.robot.sensor_reader.left_bump_sensor.read())
    while True:
        if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break

def bumpright(dc):
    print(dc.robot.sensor_reader.right_bump_sensor.read())
    while True:
        if dc.robot.sensor_reader.right_bump_sensor.read() == 0 :
            dc.robot.motor_controller.drive_pwm(0, 0)
            break

def bumpboth(dc):
    print(dc.robot.sensor_reader.left_bump_sensor.read())
    print(dc.robot.sensor_reader.right_bump_sensor.read())
    while True:
        if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
        elif dc.robot.sensor_reader.right_bump_sensor.read() == 0:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def reflectanceleft(dc):
    print(dc.robot.sensor_reader.left_reflectance_sensor.read())
    dark = dc.darkness.get()
    darknessthreshhold = int(dark)
    while True:
        if dc.robot.sensor_reader.left_reflectance_sensor.read() > darknessthreshhold:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def reflectanceright(dc):
    print(dc.robot.sensor_reader.right_reflectance_sensor.read())
    dark = dc.darkness.get()
    darknessthreshhold = int(dark)
    while True:
        if dc.robot.sensor_reader.right_reflectance_sensor.read() > darknessthreshhold:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def reflectancemiddle(dc):
    dark = dc.darkness.get()
    darknessthreshhold = int(dark)
    print(dc.robot.sensor_reader.middle_reflectance_sensor.read())
    while True:
        if dc.robot.sensor_reader.middle_reflectance_sensor.read() > darknessthreshhold:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def proximityleft(dc):
    print(dc.robot.sensor_reader.left_proximity_sensor.read())
    distance = dc.distanceleft.get()
    d = int(distance)
    while True:
        if dc.robot.sensor_reader.left_proximity_sensor.read() > d:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def proximityright(dc):
    print(dc.robot.sensor_reader.right_proximity_sensor.read())
    distance1 = dc.distanceright.get()
    d1 = int(distance1)
    while True:
        if dc.robot.sensor_reader.right_proximity_sensor.read() > d1:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def proximitymiddle(dc):
    print(dc.robot.sensor_reader.middle_proximity_sensor.read())
    distance2 = dc.distancemiddle.get()
    d2 = int(distance2)
    while True:
        if dc.robot.sensor_reader.middle_proximity_sensor.read() > d2:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def BangBangleft(dc):
    thresh = dc.threshholdentry.get()
    error = dc.errorentry.get()
    thresh1 = int(thresh)
    error1 = int(error)
    dc.robot.motor_controller.drive_pwm(30, 30)
    print(dc.robot.sensor_reader.left_reflectance_sensor.read())
    print(dc.robot.sensor_reader.right_reflectance_sensor.read())
    while True:
        if dc.robot.sensor_reader.left_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(60, 0)
        if dc.robot.sensor_reader.right_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(0, 60)
        if dc.robot.sensor_reader.right_reflectance_sensor.read() < thresh1 - error1 and dc.robot.sensor_reader.left_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break

















# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
