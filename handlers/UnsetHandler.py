import webapp2
from google.appengine.ext import db
from SetHandler import SetHandler

class UnsetHandler(webapp2.RequestHandler):
    @db.transactional
    def get(self):
        name = self.request.get('name')

        SetHandler().set_value(name, None)

        self.response.headers['Content-Type'] = 'text/plain'