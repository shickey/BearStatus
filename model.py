import datetime
import Backend.addDefault, Backend.CustomEntry, Backend.DoRun, Backend.Entry

#   To call any of these functions outside of this file, first import model
#   and then call the function by model.<function name>(...)

today = datetime.date.today()



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
    cblock = Backend.CustomEntry.CustomEntry(name = name,
                                             sTime = sTime,
                                             eTime = eTime,
                                             date = date)
    cblock.put()



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
    wday = date.isoweekday()
    q = Backend.CustomEntry.CustomEntry.all()
    q.filter("date =", date).order("sTime")
    cblocklist = []
    blocklist = []
    for block in q.run():
        cblocklist.append(block)
    if len(cblocklist) > 0:
        return cblocklist
    else:
        q = Backend.Entry.Entry.all()
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
    return getSchedule(today)


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
    Backend.addDefault.start()


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
    q = Backend.CustomEntry.CustomEntry.all()
    q.filter("date =", date).order("sTime")
    db.delete(q)