import cherrypy
from cammodule import CamModule, get_camera_list, setup_pygame_camera

class CamService(object):

    def __init__(self):
        self.camera_list = []
        setup_pygame_camera()
        camera_list = get_camera_list()
        for camera_index, camera_name in enumerate(camera_list):
            self.camera_list.append(CamModule(camera_name, camera_index))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_cameras(self):
        return {"cameraCount": 1}


    @cherrypy.expose
    def get_image(self, cam_index="0", fake="1"):
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return self.camera_list[int(cam_index)].get_bytes()
    
