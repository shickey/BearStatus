from google.appengine.ext import db

class SplitLunch(db.Model):
    name = db.LinkProperty()
    
class Feedback(db.Model):
    name = db.LinkProperty()