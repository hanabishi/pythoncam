import pygame
import tempfile
import os
from pygame import camera

# from pygame.locals import *

class CamModule:
    
    def __init__(self, index=0):
        pygame.init()
        camera.init()
        self.cam_index = index
        self.cam = camera.Camera(self.get_camera_list()[index])
        self.cam.start()
        
    def get_camera_list(self):
        return camera.list_cameras()
        
    def __get_image(self):
        return self.cam.get_image()
        
    def get_bytes(self):
        temp_file = os.path.join(tempfile.gettempdir(), "pycam%d.jpg" % self.cam_index)
        
        image = self.__get_image()
        pygame.image.save(image, temp_file)
        
        data = ""
        with open(temp_file, "rb") as reader:
            data = reader.read()
        
        os.remove(temp_file)
        
        return data
