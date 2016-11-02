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

def main():

    
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
    speedbutton = ttk.Button(frame, text='speed')
    speedbutton['command'] = (lambda:speed(speedentry, dc))

    speedentry = ttk.Entry(frame)

    bumpleftbutton = ttk.Button(frame, text='bumpleft')
    bumpleftbutton['command'] = (lambda:bumpleft(dc))
    bumprightbutton = ttk.Button(frame, text='bumpright')
    bumprightbutton['command'] = (lambda:bumpright(dc))
    bumpbothbutton = ttk.Button(frame, text='bumpboth')
    bumpbothbutton['command'] = (lambda:bumpboth(dc))

    speedbutton.grid()
    speedentry.grid()
    bumpbothbutton.grid()
    bumpleftbutton.grid()
    bumprightbutton.grid()




def speed(entry, dc):
    dc.robot = rb.RoseBot()
    myentry = entry.get()
    speed = myentry
    dc.robot.drive_pwm(speed, speed)

def bumpleft(dc):
    dc.robot = rb.RoseBot()
    dc.robot.sensor_reader.left_bump_sensor.connector.connect(5)
    if dc.robot.is_pressed() is True:
        dc.robot.drive_pwm(0, 0)

def bumpright(dc):
    dc.robot = rb.RoseBot()
    dc.robot.sensor_reader.right_bump_sensor.connector.connect(5)
    if dc.robot.is_pressed() is True:
        dc.robot.drive_pwm(0, 0)

def bumpboth(dc):
    dc.robot = rb.RoseBot()
    dc.robot.sensor_reader.right_bump_sensor.connector.connect(5)
    dc.robot.sensor_reader.left_bump_sensor.connected()
    if dc.robot.is_pressed() is True:
        dc.robot.drive_pwm(0, 0)








# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
