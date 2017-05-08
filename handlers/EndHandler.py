import webapp2
from google.appengine.ext import db, ndb
from models import Variable, Rollback

class EndHandler(webapp2.RequestHandler):
    @db.transactional
    def get(self):
        ndb.delete_multi(
            Variable.query().fetch(keys_only=True)
        )
        ndb.delete_multi(
            Rollback.query().fetch(keys_only=True)
        )

        self.response.headers['Content-Type'] = 'text/plain'