import model
import webapp2, jinja2, os, cgi
from datetime import *
from dateutil.parser import *

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'api/json')))

class APIScheduleHandler(webapp2.RequestHandler):
  
    def get(self):

        date = self.request.get('date')
        
        if date == "":
            schedule = model.getToday()
            date = model.getTime()
            display_date = "Today"
            short_date = "Today"
        else:
            date = parse(date)
            schedule = model.getSchedule(date)
            display_date = model.formatDate(date)
            short_date = date.strftime("%a %m/%d")            # short date to display in header on mobile        
            
        # check to see if the current date value is today
        is_today = (date.date() == datetime.today().date())
        
        template_values = {
            'is_today': is_today,
            'display_date': display_date,
            'schedule': schedule,
            'splitlunch': splitlunch,
            'short_date': short_date,
            'isadmin': isadmin,
            'refresh_time': refresh_time,
            'date': date,
        }
        template_values = {  

        }
        template = jinja_environment.get_template('schedule.json')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/api/schedule', APIScheduleHandler)
], debug=True)