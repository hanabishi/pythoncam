import pygame
import tempfile
import os
from pygame import camera
from threading import Lock

def get_camera_list():
    return camera.list_cameras()

def setup_pygame_camera():
    pygame.init()
    camera.init()

class CamModule:
    
    def __init__(self, camera_name, camera_index):
        self.cam_index = camera_index
        self.cam = camera.Camera(camera_name)
        self.cam.start()
        self.lock = Lock()
        
    def __get_image(self):
        return self.cam.get_image()
        
    def get_bytes(self):
        data = ""
        try:
            self.lock.acquire()
            temp_file = os.path.join(tempfile.gettempdir(), "pycam%d.jpg" % self.cam_index)
            
            image = self.__get_image()
            pygame.image.save(image, temp_file)
            
            with open(temp_file, "rb") as reader:
                data = reader.read()
            
            os.remove(temp_file)
        finally:
            self.lock.release()
        
        return data
