# request handler for editing page (/edit) goes here
# assume admin login has already been handled

import cgi
from google.appengine.api import users
import webapp2

class DateHandler(webapp2.RequestHandler):
  
  def get(self):
    date = self.request.get(date)
    name0 = self.request.get(name0)
    name1 = self.request.get(name1)
    name2 = self.request.get(name2)
    name3 = self.request.get(name3)
    name4 = self.request.get(name4)
    name5 = self.request.get(name5)
    name6 = self.request.get(name6)
    start0 = self.request.get(start0)
    start1 = self.request.get(start1)
    start2 = self.request.get(start2)
    start3 = self.request.get(start3)
    start4 = self.request.get(start4)
    start5 = self.request.get(start5)
    start6 = self.request.get(start6)
    end0 = self.request.get(end0)
    end1 = self.request.get(end1)
    end2 = self.request.get(end2)
    end3 = self.request.get(end3)
    end4 = self.request.get(end4)
    end5 = self.request.get(end5)
    end6 = self.request.get(end6)
    
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