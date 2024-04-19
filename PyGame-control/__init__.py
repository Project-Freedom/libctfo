import pygame
import sys, platform, tox

class Control:
    def __init__(self):
        self.platformCheck=platform.python_version()
        self.pygame=pygame
        self.sys=sys
    
    def checker(self):
        if (self.platformCheck >= 3.11.5):
            print("Your Python version is fully compatible!")
        else:
            print("Your Python version must be 3.11.5 or above!")
