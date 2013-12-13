# assume admin login has already been handled

import cgi
from google.appengine.api import users
import webapp2
import model
import webapp2, jinja2, os
import model
from datetime import *
from dateutil.parser import *

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class DateHandler(webapp2.RequestHandler):
  
    def get(self):
        template_values = {    
        
        }
    
        template = jinja_environment.get_template('dates.html')
        self.response.out.write(template.render(template_values))
        

class EditHandler(webapp2.RequestHandler):
            
    def get(self):
        
        # load the page with a paramater, convert it to a datetime object
        date = self.request.get('date')
        edit_date = parse('date')  
        
        # load the template
        template_values = {    
            
        }
        
        template = jinja_environment.get_template('edit.html')
        self.response.out.write(template.render(template_values))      
        
    def post(self):

        
        # requests the editing date and converts it to a datetime object
        date = self.request.get('date')
        edit_date = parse('date')
        
        iteratingblock = 0 
    
        model.deleteSchedule(edit_date)    
    
        while True:
            name = self.request.get("name" + str(iteratingblock))
            start = self.request.get("start" + str(iteratingblock))
            end = self.request.get("end" + str(iteratingblock))
            
            sTime = parse(start, default = edit_date)
            eTime = parse(end, default = edit_date)
            
            model.createBlock(name, edit_date, sTime, eTime)
            
            iteratingblock += 1
            
            if iteratingblock == 7:
                break
        
        
        # redirect to the main page
        self.redirect('/')
        
app = webapp2.WSGIApplication([
    ('/date', DateHandler),
    ('/edit', EditHandler)
], debug=True)