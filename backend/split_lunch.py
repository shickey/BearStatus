from google.appengine.ext import db

class SplitLunch(db.Model):
    name = db.LinkProperty()