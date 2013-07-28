import cv
import tempfile
import os
from threading import Lock

def get_camera_list():
    for i in range(10):
        temp_camera = cv.CreateCameraCapture(i-1)
        temp_frame = cv.QueryFrame(temp_camera)
        del(temp_camera)
        if temp_frame==None:
            del(temp_frame)
            print i
            return range(i) #MacbookPro counts embedded webcam twice

def setup_pygame_camera():
    pass

class CamModule:
    
    def __init__(self, camera_name, camera_index):
        self.cam_index = camera_index
        self.cam = cv.CaptureFromCAM(camera_index)
        cv.SetCaptureProperty(self.cam, cv.CV_CAP_PROP_FRAME_HEIGHT, 1440)
        cv.SetCaptureProperty(self.cam, cv.CV_CAP_PROP_FRAME_WIDTH, 1080)
        cv.SetCaptureProperty(self.cam, cv.CV_CAP_PROP_BRIGHTNESS,128)
        cv.SetCaptureProperty(self.cam, cv.CV_CAP_PROP_CONTRAST,128)
        self.lock = Lock()
        
    def __get_image(self):
        return cv.QueryFrame(self.cam)

    def get_bytes(self):
        data = ""
        try:
            self.lock.acquire()
            temp_file = os.path.join(tempfile.gettempdir(), "pycam%d.jpg" % self.cam_index)
            
            frame = self.__get_image()
            cv.SaveImage(temp_file,frame)
            
            with open(temp_file, "rb") as reader:
                data = reader.read()
            
            os.remove(temp_file)
        finally:
            self.lock.release()
        
        return data
