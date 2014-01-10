from google.appengine.ext import db
import datetime

class Entry(db.Model):
    name = db.StringProperty(indexed=False)
    sTime = db.TimeProperty()
    eTime = db.TimeProperty()
    day = db.IntegerProperty()
    
    def formsTime(i):
        return i.sTime.strftime("%I:%M %p")
        
    def formeTime(i):
        return i.eTime.strftime("%I:%M %p")