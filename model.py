import datetime
from google.appengine.ext import db
import backend.add_default, backend.custom_entry, backend.do_run, backend.entry, backend.split_lunch

#   To call any of these functions outside of this file, first import model
#   and then call the function by model.<function name>(...)

def formatDate(udate):
    """
    Args:
        udate:  Date to be formated (Date Object)

    Returns:
        Date in a formated string

    Description:
        This function takes a raw date object and converts it into
        a nice looking string format.
    """
    return udate.strftime("%A, %b. %d, %Y")



def formatTime(utime):
    """
    Args:
        utime:  Time to be formated (Time Object)

    Returns:
        Time in a formated string

    Description:
        This function takes a raw time object and converts it into
        a nice looking string format.
    """
    return utime.strftime("%I:%M %p")



def formatDateTime(udtime):
    """
    Args:
        udtime: Date and Time to be formated (DateTime Object)

    Returns:
        Date and Time in a formated string

    Description:
        This function takes a raw datetime object and converts it into
        a nice looking string format.
    """
    return udtime.strftime("%I:%M %p %A, %b. %d, %Y")



def changeSplitLunch(url):
    """
    Args:
        url:    URL Link to the split lunch schedule (URL)

    Returns:
        None

    Description:
        This function takes a URL Link and stores it into the datastore,
        erasing any previous link that was already there.
    """
    q = backend.split_lunch.SplitLunch.all()
    for i in q:
        db.delete(q)
    ssched = backend.split_lunch.SplitLunch(name = url)
    ssched.put()



def getSplitLunch():
    """
    Args:
        None

    Returns:
        List containing the Split Lunch URL

    Description:
        This function queries the datastore for the split lunch URL,
        and then returns it to the user.
    """
    linklist = []
    q = backend.split_lunch.SplitLunch.all()
    for i in q:
        linklist.append(i)
    
    return linklist
    
    

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