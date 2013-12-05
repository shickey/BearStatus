import cgi, datetime, yaml
from google.appengine.ext import db

# File Index
#
# Entry (class)
#       Defines a model for storing custom blocks
# doRun (class)
#       Defines a model for checking whether to add hardcoded blocks
# createTime (function)
#       Takes a number for an hour and a number for a minute and then returns the formated time
# now (function)
#       Checks if the current time is between the inputed start and end times


# Model for entering blocks into the datastore
class Entry(db.Model):
    block = db.StringProperty(indexed=False)
    sTime = db.TimeProperty()
    eTime = db.TimeProperty()
    day = db.IntegerProperty()
    
# Model for checking whether to add the hardcoded blocks to the datastore
class doRun(db.Model):
    runTrue = db.BooleanProperty()

# Returns a formated version of time
def createTime(hour, minute):
    hour = int(hour)
    minute = int(minute)
    
    return datetime.time(hour, minute)

# Checks to see whether the current time is within a time range
def now(sTime, eTime):
    current = datetime.datetime.now
    if sTime <= current:
        if eTime >= current:
            return True
        return False
    else:
        return False



# This codeblock checks whether a certain datastore entry exists, determining whether to add the hardcoded blocks to the datastore or not
q = doRun.all()
result = q.get()
if not result:
    # Creates a datastore entry to prevent readding hardcoded blocks
    hasRun = doRun(runTrue = True)
    hasRun.put()

    # Opens the tree.yaml file and saves the contents to doc
    with open('RegBlocks.yaml', 'r') as f:
        doc = yaml.load(f)
    
    # For every entry in the 'treeroot' directory of the tree.yaml file, do this:
    for x in doc['treeroot']:
        # Take the variables 'shour' and 'smin' and create a formated time stored in sTime
        sTime = datetime.time(doc['treeroot'][x]['shour'], doc['treeroot'][x]['smin'])
        # Take the variables 'ehour' and 'emin' and create a formated time stored in eTime
        eTime = datetime.time(doc['treeroot'][x]['ehour'], doc['treeroot'][x]['emin'])
        
        # Store the instance of Entry with the inputed data into entries
        entries = Entry (block = doc['treeroot'][x]['name'],
                         sTime = sTime,
                         eTime = eTime,
                         day = doc['treeroot'][x]['day'])
        # Store the data that entries contains into the datastore
        entries.put()


today = date.today()
current_weekday = today.isoweekday()

def schedule():
    blocklist = []
    q = Entry.all()
    q.filter("day =", current_weekday).order("sTime")
    for block in q.run():
        blocklist.append(block)
    return blocklist
