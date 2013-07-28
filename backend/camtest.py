'''
Created on 28 jul 2013

@author: monk
'''



import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()
image = cam.get_image()
pygame.image.save(image,"filename.jpg")