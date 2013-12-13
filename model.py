import datetime
from google.appengine.ext import db
import backend.add_default, backend.custom_entry, backend.do_run, backend.entry

#   To call any of these functions outside of this file, first import model
#   and then call the function by model.<function name>(...)

def initBlocks():
    """
    Args:
        None

    Returns:
        None

    Description:
        This function is to be called in the warmup handler of the program, to instantiate
        the entries for the default blocks into the datastore.
    """
    backend.add_default.start()



def getTime():
    """
    Args:
        None
    
    Returns:
        Python DateTime Object
    
    Description:
        This function returns the correct date and time for the specified timezone,
        including Daylight Savings Time if it is in effect
    """
    from datetime import *
    import pytz

    utcmoment_unaware = datetime.utcnow()
    utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)

    tz = 'America/Chicago'
    localDatetime = utcmoment.astimezone(pytz.timezone(tz))
    return localDatetime



def createBlock(name, date, sTime, eTime):
    """
    *NOTE*
        PLEASE RUN THE deleteSchedule FUNCTION BEFORE THIS TO AVOID DUPLICATE ENTRIES
    
    Args:
        name:   Name of the block (String)
        date:   Date of the block (Date Object)
        sTime:  Start time of the block (Time Object)
        sTime:  End time of the block (Time Object)

    Returns:
        None

    Description:
        This function is used to create and store a custom block into the datastore
    """
    cblock = backend.custom_entry.CustomEntry(name = name,
                                             sTime = sTime,
                                             eTime = eTime,
                                             date = date)
    cblock.put()



def deleteSchedule(date):
    """
    Args:
        date:   Date of the requested schedule (Date Object)

    Returns:
        None

    Description:
        This function is used to delete all special blocks that already exist for a certain day.
        The purpose of this is to prevent duplicate entries for a day. Please run this before
        running the createBlock function.
    """
    q = backend.custom_entry.CustomEntry.all()
    q.filter("date =", date).order("sTime")
    db.delete(q)



def getSchedule(date):
    """
    Args:
        date:   Date of the requested schedule (Date Object)

    Returns:
        Blocks for the inputed day, in order (List of datestore Objects)

    Description:
        This function is used to query the datastore for the schedule of any
        date. If there is a special schedule for that date, that will be returned,
        else, the default schedule for that day will be returned.
    """
    cblocklist = []
    blocklist = []
    wday = date.isoweekday()
    
    q = backend.custom_entry.CustomEntry.all()
    q.filter("date =", date).order("sTime")
    
    for block in q.run():
        cblocklist.append(block)
    
    if len(cblocklist) > 0:
        return cblocklist
    
    else:
        q = backend.entry.Entry.all()
        q.filter("day =", wday).order("sTime")
        
        for block in q.run():
            blocklist.append(block)
        
        return blocklist



def getToday():
    """
    Args:
        None

    Returns:
        Todays blocks in order (List of Objects)

    Description:
        This function is used to query the datastore for todays schedule. If there is
        a special schedule for that day, that will be returned, else the default schedule
        will be returned.
    """
    today = getTime().date()
    return getSchedule(today)