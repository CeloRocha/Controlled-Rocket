import random
import pygame

from globalVariables import (
    SETPOINT,
    G,
    X_PIXELS,
    FIRE_COLOR,
    WHITE
)
from controller import Controller
from utils import *


class Rocket(object):
    def __init__(self):
        # Properties to draw
        self.color = WHITE
        self.width = 10
        self.height = 24
        self.position = [ # In pixels
            X_PIXELS//2,
            yMetersToPixels(200)
            ]
        # PID, and pid output.
        self.controller = Controller(SETPOINT, 1)
        self.thrust = 0 # N
        # physics
        self.mass = 1 # Kg
        self.ddy = 0 # Acceleration
        self.dy = 0 # Velocity
        self.y = 200 # In meters
    def setTarget(self, target):
        self.controller.setTarget(target)
    def set_ddy(self, thrust):
        self.ddy = G + thrust/self.mass
    def get_ddy(self):
        return self.ddy
    def set_dy(self, time):
        self.dy += self.ddy * time
    def get_dy(self):
        return self.dy
    def set_y(self, time):
        self.y = (self.y + self.dy * time)
    def get_y(self):
        return self.y
    def update(self, time):
        thrust = self.controller.pdCompute(self.y, time)
        # thrust = self.controller.lqrCompute(self.y, self.dy, time)
        self.thrust = -thrust
        self.set_ddy(thrust)
        self.set_dy(time)
        self.set_y(time)
        self.position[1] = yMetersToPixels(self.y)
    def draw(self, screen):
        # Rect is draw using top left corner x, y, width and height
        pygame.draw.rect(screen, self.color, (
            self.position[0] - self.width/2,
            self.position[1] - self.height,
            self.width,
            self.height))
        pygame.draw.circle(screen, self.color, [
            self.position[0],
            self.position[1]-self.height
        ], self.width/2)
        # Fire animation
        if self.thrust > 0:
            randNum = random.randint(0,3)
            pygame.draw.polygon(screen, FIRE_COLOR, [
                [self.position[0]-self.width/2, self.position[1]],
                [self.position[0]+self.width/2, self.position[1]],
                [self.position[0], self.position[1]+self.thrust*1.5+randNum]
            ])