# assume admin login has already been handled

import model
import webapp2, jinja2, os, cgi
from datetime import *
from dateutil.parser import *

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'view/templating')))

global edit_date_datetime
global edit_date_date

class AdminHandler(webapp2.RequestHandler):
  
    def get(self):
        template_values = {    
        }
        template = jinja_environment.get_template('admin.html')
        self.response.out.write(template.render(template_values))

class DateRedirector(webapp2.RequestHandler):
  
    def get(self):
        self.redirect("admin")

class EditHandler(webapp2.RequestHandler):
            
    def get(self):

        # load the page with a paramater, convert it to a datetime object
        date = self.request.get('date')
        edit_date_datetime = parse(date)
        
        # convert the datetime object to a date object
        edit_date_date = edit_date_datetime.date()
        
        # load the template
        template_values = {    
            'edit_date': model.formatDate(edit_date_date),
        }
        
        template = jinja_environment.get_template('edit.html')
        self.response.out.write(template.render(template_values))      
        
    def post(self):

        date = self.request.get('date')
        edit_date_datetime = parse(date)
        
        # convert the datetime object to a date object
        edit_date_date = edit_date_datetime.date()
        
        # delete any existing schedules to prevent duplicates
        model.deleteSchedule(edit_date_date)    
        
        iteratingblock = 0
    
        while True:
            
            name = self.request.get("name" + str(iteratingblock))
            
            if name != "":
                
                # get values from form
                sHour = self.request.get("sHour" + str(iteratingblock))
                sMinute = self.request.get("sMinute" + str(iteratingblock))
                eHour = self.request.get("eHour" + str(iteratingblock))
                eMinute = self.request.get("eMinute" + str(iteratingblock))
                sT = self.request.get("sT" + str(iteratingblock))
                eT = self.request.get("eT" + str(iteratingblock))
                
                # parse input to datetime obejcts
                sTime_dt = parse(str(sHour) + "h" + str(sMinute) + "m" + " " + str(sT))
                eTime_dt = parse(str(eHour) + "h" + str(eMinute) + "m" + " " + str(eT))
                
                # convert input to time objects
                sTime = sTime_dt.time()
                eTime = eTime_dt.time()
                
                # write block to datastore
                model.createBlock(name, edit_date_date, sTime, eTime)

            # if name != "":
                
            #     start = self.request.get("start" + str(iteratingblock))
            #     end = self.request.get("end" + str(iteratingblock))
                
            #     # parse start and end time inputs
            #     sTime_dt = parse(start, default = edit_date_datetime)
            #     eTime_dt = parse(end, default = edit_date_datetime)
                
            #     # convert datetime objects to time objects
            #     sTime = sTime_dt.time()
            #     eTime = eTime_dt.time()
                
            #     # run through backend code
            #     model.createBlock(name, edit_date_date, sTime, eTime)
            
            iteratingblock += 1
            
            if iteratingblock == 12:
                break
                
        # redirect to the main page
        self.redirect('/')
        

class SplitLunchHandler(webapp2.RequestHandler):
    
    def get(self):

        date = self.request.get('lunchurl')
        model.changeSplitLunch(date)
        
        self.redirect('/')

class RevertDateHandler(webapp2.RequestHandler):
    
    def get(self):
        
        date = self.request.get('dateR')
        
        edit_date_datetime = parse(date)
        
        model.deleteSchedule(edit_date_datetime)
        
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/date', DateRedirector),
    ('/edit', EditHandler),
    ('/revertdate', RevertDateHandler),
    ('/admin', AdminHandler),
    ('/changelunch', SplitLunchHandler)
], debug=True)