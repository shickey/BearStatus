from google.appengine.ext import db
import datetime, os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
import model

class CustomEntry(db.Model):
    name = db.StringProperty(indexed=False)
    sTime = db.TimeProperty()
    eTime = db.TimeProperty()
    date = db.DateProperty()
    tooltip = db.StringProperty(indexed=False)

    def formsTime(i):
        return i.sTime.strftime("%I:%M %p")
        
    def formeTime(i):
        return i.eTime.strftime("%I:%M %p")

    def isnow(i):
        now = model.getTime().time()
        if i.sTime <= now and i.eTime >= now:
            return True
        return False
            
    def sTimeMinutes(self):
        return (self.sTime.hour * 60) + self.sTime.minute
    
    def eTimeMinutes(self):
        return (self.eTime.hour * 60) + self.eTime.minute