# Import blockmodels file
import model, controller
import webapp2, jinja2, os
from datetime import *
from dateutil.parser import *
from google.appengine.api import users

# initalize the blocks
model.initBlocks()
blocks_initialized = True

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'view/templating')))
    
class MainHandler(webapp2.RequestHandler):
    
    def get(self):
            
        schedule = model.getToday()
        block = controller.current_block(schedule)
        blocksTime = controller.testsblock(block)
        blockeTime = controller.testeblock(block)
        the_next_block = controller.next_block(schedule)
        next_blocksTime = controller.testsblock(the_next_block)
        next_blockeTime = controller.testeblock(the_next_block)
        
        # admin check for navbar
        isadmin = users.is_current_user_admin()
        
        # determine the page title
        if block:
          title = blockeTime + ": End " + block.name
        elif the_next_block:
          title = next_blocksTime + ": Start " + the_next_block.name
        else:
          title = "BearStatus"
          
        # determine whether or not to refresh, and if so, what time to do it at
        if block:
            refresh_time = block.eTime.strftime("%H,%M,01")
        elif the_next_block:
            refresh_time = the_next_block.sTime.strftime("%H,%M,01")
            
        
        template_values = {
            'block': block,
            'blocksTime': blocksTime,
            'blockeTime': blockeTime,
            'next_blocksTime': next_blocksTime,
            'next_blockeTime': next_blockeTime,
            'next_block': the_next_block,
            'isadmin': isadmin,
            'title': title,
            'refresh_time': refresh_time,
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))


class Schedule_Handler(webapp2.RequestHandler):
    
    def get(self):

        date = self.request.get('date')
        splitlunch = model.getSplitLunch()
        
        if date == "":
            schedule = model.getToday()
            date = model.getTime()
            display_date = "Today"
        else:
            date = parse(date)
            schedule = model.getSchedule(date)
            display_date = model.formatDate(date)
        
        short_date = date.strftime("%x")            # short date to display in form at bottom
           
        # admin check for navbar
        isadmin = users.is_current_user_admin()
            
        template_values = {
            'display_date': display_date,
            'schedule': schedule,
            'splitlunch': splitlunch,
            'short_date': short_date,
            'isadmin': isadmin
        }

        template = jinja_environment.get_template('schedule.html')
        self.response.out.write(template.render(template_values))
        
class AboutHandler(webapp2.RequestHandler):
  
    def get(self):
        
        # admin check for navbar
        isadmin = users.is_current_user_admin()
        
        template_values = {    
            'isadmin': isadmin
        }
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render(template_values))
        
# this runs as a new instance of an app is loaded to load the blocks
# it reduces load times and improves scalability
class WarmupHandler(webapp2.RequestHandler):
    
    def get(self):
        
        global blocks_initialized
        
        # initialize the blocks if this hasn't been done
        if blocks_initialized != True:
            model.initBlocks()
            blocks_initialized = True

class LunchLinkHandler(webapp2.RequestHandler):
    
    def get(self):
        splitlunch = model.getSplitLunch()
        if len(splitlunch) > 0:
            self.redirect(str(splitlunch[0].name))
        else:
            self.redirect("404.derp")
        

# class DebugHandler(webapp2.RequestHandler):
    
#     def get(self):
#         isadmin = model.isadmin()
#         self.response.write(isadmin)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/schedule', Schedule_Handler),
    ('/about', AboutHandler),
    ('/_ah/warmup', WarmupHandler),
    ('/splitlunch', LunchLinkHandler),
    ('/specificday', Schedule_Handler),
    # ('/debug', DebugHandler)
], debug=True)


