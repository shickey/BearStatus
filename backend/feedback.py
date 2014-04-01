from google.appengine.ext import db

class Feedback(db.Model):
    name = db.LinkProperty()