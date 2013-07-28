import os
import platform
import cherrypy
import logging
import cam
#from cherrypy.process.plugins import Daemonizer, PIDFile

class Root(object):

    @cherrypy.expose
    def index(self):
        if os.path.exists("../frontend/index.html"):
            raise cherrypy.HTTPRedirect("index.html")
        else:
            return "Index.html not found"

class WebService(object):

    @cherrypy.expose
    def index(self):
        return "Index of the webservices"
    
if __name__ == "__main__":
    session_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", "sessions")


    if not os.path.exists(session_path):
        os.makedirs(session_path)

    config = {'global': {'server.socket_host': '0.0.0.0'},
              '/': {'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
                          'tools.sessions.on' : True,
                          'tools.sessions.storage_type' : "file",
                          'tools.sessions.storage_path' : session_path,
                          'tools.sessions.timeout' : 60,
    					  'tools.staticdir.on': True,
                          'tools.staticdir.dir': '../frontend'}}
    
    
    ## Add more webservices when needed
    root = Root()
    root.webservice = WebService()
    root.webservice.cam = cam.Cam()
    
    cherrypy.quickstart(root, '/', config=config)
