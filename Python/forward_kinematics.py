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

    def calculate_b(self):
        '''
        Calculates point b by converting from polar to cartesian coordinates
        '''

        b = (self.a[0] + self.r * math.cos(self.theta), self.a[1] - self.r * math.sin(self.theta)) # x = r * cos(theta), y = r * sin(theta)
        return b

    def draw_segment(self):
        '''
        Draws segment to screen with assigned attributes
        '''

        pygame.draw.line(SCREEN, self.colour, self.a, self.b, self.width)

    def wiggle(self, i, t):
        '''
        Sinsuoidal wiggle function - varies offset with time, dependent on position in hierarchy
        '''

        self.offset =  i * (math.sin(t * 0.5 * i) / (i + 1))

    def update(self, i, t):
        '''
        Updates the segment by applying wiggle, recalculating point b and incrementing the theta value
        '''

        self.wiggle(i, t)
        self.b = self.calculate_b()
        self.theta += self.offset

class SegmentChild(SegmentParent):

    '''
    SEGMENT CHILD CLASS:

    - inherits methods from SegmentParent
    - used for all segments not attached to a fixed point
    - 
    '''
