from google.appengine.ext import db

class Entry(db.Model):
    name = db.StringProperty(indexed=False)
    sTime = db.TimeProperty()
    eTime = db.TimeProperty()
    day = db.IntegerProperty()
    
class doRun(db.Model):
    runTrue = db.BooleanProperty()

class CustomEntry(db.Model):
    name = db.StringProperty(indexed=False)
    sTime = db.TimeProperty()
    eTime = db.TimeProperty()
    day = db.IntegerProperty()