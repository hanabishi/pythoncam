import cherrypy
from cammodule import CamModule, get_camera_list, setup_camera

class CamService(object):

    def __init__(self, root):
        self.camera_list = {}
        setup_camera()
        self.camera_index_list = get_camera_list()
        for camera_index in self.camera_index_list:
            self.camera_list[camera_index] = CamModule(camera_index)
            self.camera_list[camera_index].start()
        root.set_camservice(self)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_cameras(self):
        return {"cameraIndexes": self.camera_index_list}

    def shutdown(self):
        for camera in self.camera_list:
            self.camera_list[camera].is_running = False
        for camera in self.camera_list:
            while self.camera_list[camera].is_alive():
                pass
            
            


    @cherrypy.expose
    def get_image(self, cam_index="0", fake="1"):
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return self.camera_list[int(cam_index)].get_image()
    
