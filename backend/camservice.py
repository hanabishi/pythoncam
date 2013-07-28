import cherrypy
from cammodule import CamModule

class CamService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_cameras(self):
        return {"cameras": [{"cameraname":"0", "cameraIndex":0}, {"cameraname":"/dev/youSuckSoHard", "cameraIndex":1}]}


    @cherrypy.expose
    def get_image(self, cam_index="0", fake="1"):
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return CamModule(int(cam_index)).get_bytes()
    
