import numpy as np
from enum import Enum
import pygame

####################################################################################
#                           System class begins
####################################################################################

# Conceptually, all entities in the simulation are systems. For this reason,
# other classes inherit from this one.
# In the current implementation, this is not strictly necessary, as not all
# classes share properties with this one.
class System:
    # construct System. Many systems have xy-coordinates and orientations (theta), but for some, such as Controllers and Disturbances, it is
    # not useful to give them these variables. For those systems, has_position and/or has_orientation are set to false
    def __init__(self, x=None, y=None, theta=None):
        self.has_position = not (x is None or y is None)
        if self.has_position:
            self.x = x
            self.y = y
            self.xs = [x]
            self.ys = [y]
        self.has_orientation = theta is not None
        if self.has_orientation:
            self.theta = theta
            self.thetas = [theta]

    # systems with position and/or orientation will *need* to call this method,
    # from their own step method
    def step(self, dt):
        if self.has_position:
            self.xs.append(self.x)
            self.ys.append(self.y)
        if self.has_orientation:
            self.thetas.append(self.theta)


####################################################################################
#                           System class ends
####################################################################################

####################################################################################
#                           Agent classes begin
####################################################################################


class Agent(System):

    def __init__(self, x, y, theta=None):
        super().__init__(x, y, theta)  # call System constructor. xy-variables are handled there

    # Agent has no step, so if one of its subclasses makes a call to super().step,
    # then the call will go to System.step()

####################################################################################
#                           Agent classes end
####################################################################################
