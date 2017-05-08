import webapp2
from handlers import GetHandler, SetHandler, UnsetHandler, NumEqualToHandler, UndoHandler, EndHandler

application = webapp2.WSGIApplication([
    ('/get', GetHandler),
    ('/set', SetHandler),
    ('/unset', UnsetHandler),
    ('/numequalto', NumEqualToHandler),
    ('/undo', UndoHandler),
    ('/end', EndHandler)
], debug=False)