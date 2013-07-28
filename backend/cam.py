import cherrypy

class Cam(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_lost(self):
        return {"getLost": "is a word"}


    @cherrypy.expose
    def get_picture(self, cam_index="1"):
        return "dasdsadasdasdasdsadas" + cam_index
