# Import blockmodels file
import model
import webapp2, jinja2, os
from datetime import *
from dateutil.parser import *

blocks_initialized = False

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'view/templating')))

def now(sTime, eTime):
    current = model.getTime().time()
    if current >= sTime and current <= eTime:
        return True
    else:
        return False

# given a schedule list, determine the current block and return its model
def current_block(schedule_list):
    for i in schedule_list:
        if i.isnow() == True:
            return i

def next_block(schedule_list):
    current = model.getTime().time()
    for i in schedule_list:
        if current <= i.sTime:
            return i

def testsblock(block):
    # try:
    #     block.isnow()
    # except RuntimeError:
    #     return ""
    # return block.formsTime()
    if block == None:
        return ""
    return block.formsTime()

def testeblock(block):
    # try:
    #     block.isnow()
    # except RuntimeError:
    #     return ""
    # return block.formeTime()
    if block == None:
        return ""
    return block.formeTime()
    
class MainHandler(webapp2.RequestHandler):
    
    def get(self):
        
        global blocks_initialized
        
        # initialize the blocks if this hasn't been done
        if blocks_initialized != True:
            model.initBlocks()
            blocks_initialized = True
            
        schedule = model.getToday()
        block = current_block(schedule)
        blocksTime = testsblock(block)
        blockeTime = testeblock(block)
        the_next_block = next_block(schedule)
        next_blocksTime = testsblock(the_next_block)
        next_blockeTime = testeblock(the_next_block)
        template_values = {
            'block': block,
            'blocksTime': blocksTime,
            'blockeTime': blockeTime,
            'next_blocksTime': next_blocksTime,
            'next_blockeTime': next_blockeTime,
            'next_block': the_next_block,
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
            
        template_values = {
            'display_date': display_date,
            'schedule': schedule,
            'splitlunch': splitlunch,
            'short_date': short_date,
        }

        template = jinja_environment.get_template('schedule.html')
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
        

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/schedule', Schedule_Handler),
    ('/_ah/warmup', WarmupHandler),
    ('/splitlunch', LunchLinkHandler),
    ('/specificday', Schedule_Handler),
], debug=True)


