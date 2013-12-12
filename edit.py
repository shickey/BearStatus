# request handler for editing page (/edit) goes here
# assume admin login has already been handled

import cgi
from google.appengine.api import users
import webapp2

class DateHandler(webapp2.RequestHandler):
  
  def get(self):
    date = self.request.get(date)
    template_values = {    
        
    }
    
    template = jinja_environment.get_template('dates.html')
    self.response.out.write(template.render(template_values))

class EditHandler(webapp2.RequestHandler):
  
  def get(self):
    
    template_values = {    
        
    }
    
    template = jinja_environment.get_template('edit.html')
    self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/date', DateHandler)
    ('/edit', EditHandler)
], debug=True)