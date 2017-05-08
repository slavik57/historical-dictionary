import webapp2
from models import Variable

class NumEqualToHandler(webapp2.RequestHandler):
    def get(self):
        value = self.request.get('value')

        query = Variable.query(Variable.value == value)
        total = query.count()

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(total)