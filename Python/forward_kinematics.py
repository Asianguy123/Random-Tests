# Forward Kinematics

'''
Using forward kinematics to create tentacle oscillation (sinusoidal)
FK uses joint hierarchy e.g. upper leg > lower leg > foot > toes
'''
# ---------------------------------------------------------------------------------------------------------------------
# Imports

import sys
import pygame
import math

# ---------------------------------------------------------------------------------------------------------------------
# Segement Classes

class SegmentParent():

    '''
    SEGMENT PARENT CLASS:

    - creates a root segment from all other segments are joined from
    - pivots around a fixed point
    - calculations of segment end points done via polar-cartesian conversion
    '''
    
    def __init__(self, x, y, length, angle, width, colour):
        self.a = (x, y)
        self.r = length
        self.theta = angle
        self.width = width
        self.colour = colour
        self.offset = 0
