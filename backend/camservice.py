import cherrypy
from cammodule import CamModule

class CamService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_lost(self):
        return {"getLost": "is a word"}


    @cherrypy.expose
    def get_image(self, cam_index="0", fake="1"):
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return CamModule(int(cam_index)).get_bytes()
    
    
#    def index(self):
#    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
#    
#
#    buffer = StringIO.StringIO()
#    surface.write_to_png(buffer)
#    buffer.seek(0)
#
#    return file_generator(buffer)

