from google.appengine.ext import db

class CustomEntry(db.Model):
    name = db.StringProperty(indexed=False)
    sTime = db.TimeProperty()
    eTime = db.TimeProperty()
    date = db.DateProperty()

    def formsTime(i):
        return i.sTime.strftime("%I:%M %p")
        
    def formeTime(i):
        return i.eTime.strftime("%I:%M %p")