from google.appengine.ext import db

class CustomEntry(db.Model):
    name = db.StringProperty(indexed=False)
    sTime = db.TimeProperty()
    eTime = db.TimeProperty()
    date = db.DateProperty()