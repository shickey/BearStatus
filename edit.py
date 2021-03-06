# assume admin login has already been handled

import model
import webapp2, jinja2, os, cgi
from datetime import *
from dateutil.parser import *
from google.appengine.api import users

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'view/templating')))

class AdminHandler(webapp2.RequestHandler):
  
    def get(self):
        
        # admin check for navbar
        isadmin = users.is_current_user_admin()
        
        template_values = {  
        'isadmin': isadmin, 
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
        
        # determine how many blocks are needed
        blocks = self.request.get('blocks')
        if blocks == "":
            blocks = 12
        else:
            blocks = int(blocks)
            
        # figure out if there is a special schdedule already to display warning
        is_special = model.isSpecialSchedule(edit_date_date)

        # admin check for navbar
        isadmin = users.is_current_user_admin()
                
        # load the template
        template_values = {    
            'edit_date': model.formatDate(edit_date_date),
            'blocks': blocks,
            'isadmin': isadmin,
            'is_special': is_special
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
        
        maxblocks = self.request.get('blocks')
        if maxblocks == "":
            maxblocks = 12
        else:
            maxblocks = int(maxblocks)
        
        iteratingblock = 0
    
        while True:
            
            # pull block name and optional tooltip from form
            name = self.request.get("name" + str(iteratingblock))

            if name != "":
                
                tooltip = self.request.get("tooltip" + str(iteratingblock))
                start = self.request.get("start" + str(iteratingblock))
                end = self.request.get("end" + str(iteratingblock))
                
                # parse start and end time inputs
                sTime_dt = parse(start, default = edit_date_datetime)
                eTime_dt = parse(end, default = edit_date_datetime)
                
                # convert datetime objects to time objects
                sTime = sTime_dt.time()
                eTime = eTime_dt.time()
                
                # run through backend code
                model.createBlock(name, edit_date_date, sTime, eTime, tooltip)
            
            iteratingblock += 1
            
            if iteratingblock == maxblocks:
                break
                
        # redirect to the schedule for the date just edited
        self.redirect('/schedule?date=' + date)
        

class SplitLunchHandler(webapp2.RequestHandler):
    
    def get(self):

        date = self.request.get('lunchurl')
        model.changeSplitLunch(date)
        
        self.redirect('/')

class FeebackWriteHandler(webapp2.RequestHandler):
    
    def get(self):

        url = self.request.get('feedbackurl')
        model.changeFeedback(url)
        
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
    ('/changelunch', SplitLunchHandler),
    ('/changefeedback', FeebackWriteHandler)
], debug=True)