import cv
import os
import time
from threading import Lock
from threading import Thread

def get_camera_list():
    cameras = []
    for i in range(10):
        temp_camera = cv.CreateCameraCapture(i)
        temp_frame = cv.QueryFrame(temp_camera)
        cameraFailure = cv.GetCaptureProperty(temp_camera, cv.CV_CAP_PROP_FRAME_WIDTH) == 0.0 or cv.GetCaptureProperty(temp_camera, cv.CV_CAP_PROP_FRAME_HEIGHT) == 0.0
        if temp_camera != None and temp_frame != None and not cameraFailure:
            cameras.append(i);
        del(temp_camera)
        del(temp_frame)
    return cameras

def setup_camera():
    pass

class CamModule(Thread):
    
    def __init__(self, camera_index):
        
        Thread.__init__(self);
        self.is_running = True
        self.cam_index = camera_index
        self.cam = cv.CaptureFromCAM(camera_index)
        cv.SetCaptureProperty(self.cam, cv.CV_CAP_PROP_FRAME_HEIGHT, 1440)
        cv.SetCaptureProperty(self.cam, cv.CV_CAP_PROP_FRAME_WIDTH, 1080)
        self.cache_files = {}
        self.cache_files[0]={"filename":os.path.join("cache", "py0cam%d.jpg" % self.cam_index), "counter":0}
        self.cache_files[1]={"filename":os.path.join("cache", "py1cam%d.jpg" % self.cam_index), "counter":0}
        self.track = 0
        self.lock = Lock()
        
    def run(self):
        while self.is_running:
            try:
                self.lock.acquire()
                t = self.track
                self.track = (self.track + 1) % 2
            finally:
                self.lock.release()
            while self.cache_files[t]["counter"] > 0:
                time.sleep(0.1);
            frame = cv.QueryFrame(self.cam)
            cv.SaveImage(self.cache_files[t]["filename"], frame)
            
            time.sleep(0.1)

    def get_image(self):
            data=''
            try:
                self.lock.acquire()
                t = self.track
                self.cache_files[t]["counter"]+=1
                self.lock.release()
                with open(self.cache_files[t]["filename"],"r") as reader:
                    data=reader.read()            
            
            finally:
                self.lock.acquire()
                self.cache_files[t]["counter"]-=1
                self.lock.release()
            
            return data
