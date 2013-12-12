# Import blockmodels file
import model
import webapp2, jinja2, os
from datetime import *

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


# Use this function to get the current date and time
def getTime():
    import pytz

    utcmoment_unaware = datetime.utcnow()
    utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)

    tz = 'America/Chicago'

    localDatetime = utcmoment.astimezone(pytz.timezone(tz))
    return localDatetime

def now(sTime, eTime):
    current = getTime().time()
    if current >= sTime and current <= eTime:
        return True
    else:
        return False

# given a schedule list, determine the current block and return its model
def current_block(schedule_list):
    for i in schedule_list:
        if now(i.sTime,i.eTime) == True:
            return i

class MainHandler(webapp2.RequestHandler):
    def get(self):
        schedule = model.getToday()
        block = current_block(schedule)
        template_values = {
            'block': block,
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))


class Schedule_Handler(webapp2.RequestHandler):
    def get(self):
        schedule = model.getToday()
        tlocal = getTime()
        formNow = datetime.strftime(tlocal, "%A, %b %d %I:%M:%S %p")
        template_values = {
            'schedule': schedule,
            'localtime': formNow,
        }

        template = jinja_environment.get_template('schedule.html')
        self.response.out.write(template.render(template_values))
        
# this runs as a new instance of an app is loaded to load the blocks
# it reduces load times and improves scalability
class WarmupHandler(webapp2.RequestHandler):
    def get(self):
      model.initBlocks()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/schedule', Schedule_Handler),
    ('/_ah/warmup', WarmupHandler)
], debug=True)


