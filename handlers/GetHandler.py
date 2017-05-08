import webapp2
from models import Variable

class GetHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')

        query = Variable.query(Variable.name == name)
        variable = query.get(projection=[Variable.value])

        self.response.headers['Content-Type'] = 'text/plain'
        if variable is None:
            self.response.write('None')
        else:
            self.response.write(variable.value)
