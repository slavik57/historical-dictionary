import webapp2
from google.appengine.ext import db
from models import Variable, Rollback

class UndoHandler(webapp2.RequestHandler):
    @db.transactional
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        rollback = Rollback.query().order(-Rollback.date).get()

        if rollback is None:
            self.response.write('NO COMMANDS')
            return

        variable = Variable.query(Variable.name == rollback.name).get()
        variable.value = rollback.value

        variable.put()
        rollback.key.delete()