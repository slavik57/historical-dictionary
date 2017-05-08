from google.appengine.ext import ndb

class Variable(ndb.Model):
    name = ndb.StringProperty(indexed=True)
    value = ndb.StringProperty(indexed=True)