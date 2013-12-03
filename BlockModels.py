import cgi, datetime
from google.appengine.ext import ndb
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
    runTrue = ndb.BooleanProperty()

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



# Hardcoded Blocks

# This codeblock checks whether a certain datastore entry exists, determining whether to add the hardcoded blocks to the datastore or not
q = doRun.all()
result = q.get()
if not result:
    # Creates a datastore entry to prevent readding hardcoded blocks
    hasRun = doRun(runTrue = True)
    hasRun.put()




# Monday
    # Create the formated times
    sTime = datetime.time(8, 00)
    eTime = datetime.time(8, 45)
    # Store the instance of the class Entry in entries, with entered data
    entries = Entry (block = "Block 1",
                    sTime = sTime,
                    eTime = eTime,
                    day = 1)
    # Stores the data that entries contains into the datastore
    entries.put()



    sTime = datetime.time(8, 50)
    eTime = datetime.time(9, 35)
    entries = Entry (block = "Block 2",
                    sTime = sTime,
                    eTime = eTime,
                    day = 1)
    entries.put()
    
    
    
    sTime = datetime.time(9, 40)
    eTime = datetime.time(10, 15)
    entries = Entry (block = "Tutorial",
                    sTime = sTime,
                    eTime = eTime,
                    day = 1)
    entries.put()



    sTime = datetime.time(10, 20)
    eTime = datetime.time(11, 05)
    entries = Entry (block = "Block 3",
                    sTime = sTime,
                    eTime = eTime,
                    day = 1)
    entries.put()



    sTime = datetime.time(11, 10)
    eTime = datetime.time(12, 30)
    entries = Entry (block = "Block 4/Lunch",
                    sTime = sTime,
                    eTime = eTime,
                    day = 1)
    entries.put()



    sTime = datetime.time(12, 35)
    eTime = datetime.time(13, 20)
    entries = Entry (block = "Block 5",
                    sTime = sTime,
                    eTime = eTime,
                    day = 1)
    entries.put()



    sTime = datetime.time(13, 25)
    eTime = datetime.time(14, 10)
    entries = Entry (block = "Block 6",
                    sTime = sTime,
                    eTime = eTime,
                    day = 1)
    entries.put()



    sTime = datetime.time(14, 15)
    eTime = datetime.time(15, 00)
    entries = Entry (block = "Block 7",
                    sTime = sTime,
                    eTime = eTime,
                    day = 1)



# Tuesday

    sTime = datetime.time(8, 00)
    eTime = datetime.time(9, 05)
    entries = Entry (block = "Block 2",
                    sTime = sTime,
                    eTime = eTime,
                    day = 2)
    entries.put()



    sTime = datetime.time(9, 10)
    eTime = datetime.time(9, 45)
    entries = Entry (block = "Assembly",
                    sTime = sTime,
                    eTime = eTime,
                    day = 2)
    entries.put()



    sTime = datetime.time(9, 50)
    eTime = datetime.time(10, 55)
    entries = Entry (block = "Block 4",
                    sTime = sTime,
                    eTime = eTime,
                    day = 2)
    entries.put()



    sTime = datetime.time(11, 00)
    eTime = datetime.time(12, 40)
    entries = Entry (block = "Block 3/Lunch",
                    sTime = sTime,
                    eTime = eTime,
                    day = 2)
    entries.put()



    sTime = datetime.time(12, 45)
    eTime = datetime.time(13, 50)
    entries = Entry (block = "Block 7",
                    sTime = sTime,
                    eTime = eTime,
                    day = 2)
    entries.put()



    sTime = datetime.time(13, 55)
    eTime = datetime.time(15, 00)
    entries = Entry (block = "Block 6",
                    sTime = sTime,
                    eTime = eTime,
                    day = 2)
    entries.put()



# Wednesday

    sTime = datetime.time(8, 30)
    eTime = datetime.time(9, 35)
    entries = Entry (block = "Block 1",
                    sTime = sTime,
                    eTime = eTime,
                    day = 3)
    entries.put()
    
    

    sTime = datetime.time(9, 40)
    eTime = datetime.time(10, 10)
    entries = Entry (block = "Advisory/Grade Meeting",
                    sTime = sTime,
                    eTime = eTime,
                    day = 3)
    entries.put()



    sTime = datetime.time(10, 15)
    eTime = datetime.time(11, 20)
    entries = Entry (block = "Block 2",
                    sTime = sTime,
                    eTime = eTime,
                    day = 3)
    entries.put()



    sTime = datetime.time(11, 25)
    eTime = datetime.time(13, 05)
    entries = Entry (block = "Block 5/Lunch",
                    sTime = sTime,
                    eTime = eTime,
                    day = 3)
    entries.put()



    sTime = datetime.time(13, 10)
    eTime = datetime.time(13, 50)
    entries = Entry (block = "TASC/Symposium",
                    sTime = sTime,
                    eTime = eTime,
                    day = 3)
    entries.put()



    sTime = datetime.time(13, 55)
    eTime = datetime.time(15, 00)
    entries = Entry (block = "Block 6",
                    sTime = sTime,
                    eTime = eTime,
                    day = 3)
    entries.put()



# Thursday

    sTime = datetime.time(8, 00)
    eTime = datetime.time(9, 05)
    entries = Entry (block = "Block 3",
                    sTime = sTime,
                    eTime = eTime,
                    day = 4)
    entries.put()



    sTime = datetime.time(9, 10)
    eTime = datetime.time(9, 45)
    entries = Entry (block = "Assembly",
                    sTime = sTime,
                    eTime = eTime,
                    day = 4)
    entries.put()



    sTime = datetime.time(9, 50)
    eTime = datetime.time(10, 55)
    entries = Entry (block = "Block 1",
                    sTime = sTime,
                    eTime = eTime,
                    day = 4)
    entries.put()



    sTime = datetime.time(11, 00)
    eTime = datetime.time(12, 40)
    entries = Entry (block = "Block 4/Lunch",
                    sTime = sTime,
                    eTime = eTime,
                    day = 4)
    entries.put()



    sTime = datetime.time(12, 45)
    eTime = datetime.time(13, 50)
    entries = Entry (block = "Block 5",
                    sTime = sTime,
                    eTime = eTime,
                    day = 4)
    entries.put()



    sTime = datetime.time(13, 55)
    eTime = datetime.time(15, 00)
    entries = Entry (block = "Block 7",
                    sTime = sTime,
                    eTime = eTime,
                    day = 4)
    entries.put()



# Friday

    sTime = datetime.time(8, 30)
    eTime = datetime.time(9, 15)
    entries = Entry (block = "Block 2",
                    sTime = sTime,
                    eTime = eTime,
                    day = 5)
    entries.put()



    sTime = datetime.time(9, 20)
    eTime = datetime.time(10, 05)
    entries = Entry (block = "Block 1",
                    sTime = sTime,
                    eTime = eTime,
                    day = 5)
    entries.put()



    sTime = datetime.time(10, 10)
    eTime = datetime.time(10, 55)
    entries = Entry (block = "Block 3",
                    sTime = sTime,
                    eTime = eTime,
                    day = 5)
    entries.put()



    sTime = datetime.time(11, 00)
    eTime = datetime.time(12, 30)
    entries = Entry (block = "Block 4/Lunch",
                    sTime = sTime,
                    eTime = eTime,
                    day = 5)
    entries.put()
    
    

    sTime = datetime.time(12, 35)
    eTime = datetime.time(13, 20)
    entries = Entry (block = "Block 6",
                    sTime = sTime,
                    eTime = eTime,
                    day = 5)
    entries.put()



    sTime = datetime.time(13, 25)
    eTime = datetime.time(14, 10)
    entries = Entry (block = "Block 7",
                    sTime = sTime,
                    eTime = eTime,
                    day = 5)
    entries.put()



    sTime = datetime.time(14, 15)
    eTime = datetime.time(15, 00)
    entries = Entry (block = "Block 5",
                    sTime = sTime,
                    eTime = eTime,
                    day = 5)
    entries.put()