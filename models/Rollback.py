from google.appengine.ext import ndb

class Rollback(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    value = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
