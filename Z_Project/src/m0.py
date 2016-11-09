"""
The Python Capstone Project.

This file contains data SHARED by the other modules in this project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).
"""
# TODO: Put the names of ALL team members in the above where indicated.

import m1
import m2
import m3
import m4

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb

# ----------------------------------------------------------------------
# TODO: TEAM-PROGRAM this module so that it runs your entire program,
#       incorporating parts from m1 .. m3.
# ----------------------------------------------------------------------

class DataContainer(object, metaclass=rb.__FreezeClass__):
    """
    A container for the data shared across the application.
    Remember to CONSTRUCT a DataContainer with:
       dc = DataContainer()
    """
    def __init__(self):
        """ Initializes instance variables (fields). """
        # Add     self.FOO = BLAH     here as needed.
        # Choose meaningful names!
        self.demo = 'demo'
        self.robot = rb.RoseBot()
        self.time_cliked = 0





def main():
    """ Runs the MAIN PROGRAM. """
    print('----------------------------------------------')
    print('Integration Testing of the INTEGRATED PROGRAM:')
    print('----------------------------------------------')
    my_dc = DataContainer()
    root = tkinter.Tk()
    m1.my_frame(root, my_dc)
    m2.my_frame(root, my_dc)
    m3.my_frame(root, my_dc)
    m4.my_frame(root, my_dc)

    root.mainloop()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
