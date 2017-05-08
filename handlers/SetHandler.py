import webapp2
from google.appengine.ext import db
from models import Variable, Rollback

class SetHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')
        value = self.request.get('value')

        self.set_value(name, value)

        self.response.headers['Content-Type'] = 'text/plain'

    @db.transactional
    def set_value(self, name, value):
        variable = Variable.query(Variable.name == name).get()
        if variable is None:
            variable = Variable(name=name,value=value)
            rollback = Rollback(name=name, value=None)
        else:
            rollback = Rollback(name=name, value=variable.value)
            variable.value = value

        rollback.put()
        variable.put()
