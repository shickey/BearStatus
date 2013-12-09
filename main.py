# Import blockmodels file
import BlockModels
import webapp2, jinja2, os
from datetime import *

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class CST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=-6)

    def tzname(self, dt):
        return "US/Central"

    def dst(self, dt):
        return timedelta(0)
        
cst = CST()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'block': block,
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class Schedule_Handler(webapp2.RequestHandler):
    def get(self):
        schedule = BlockModels.schedule()
        tlocal = datetime.now(cst)
        formNow = datetime.strftime(tlocal, "%A, %b %d %I:%M:%S %p")
        template_values = {
            'schedule': schedule,
            'localtime': formNow,
        }

        template = jinja_environment.get_template('schedule.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ('/schedule', Schedule_Handler)
], debug=True)


