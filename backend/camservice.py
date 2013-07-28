import cherrypy
from cammodule import CamModule, get_camera_list, setup_pygame_camera

class CamService(object):

    def __init__(self):
        self.camera_list = []
        setup_pygame_camera()
        for camera_index in get_camera_list():
            self.camera_list.append(CamModule(camera_index, camera_index))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_cameras(self):
        return {"cameraCount": 1}


    @cherrypy.expose
    def get_image(self, cam_index="0", fake="1"):
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return self.camera_list[int(cam_index)].get_bytes()
    
