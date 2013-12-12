import datetime
import Backend.addDefault, Backend.CustomEntry, Backend.DoRun, Backend.Entry

#   To call any of these functions outside of this file, first import model
#   and then call the function by model.<function name>(...)

today = datetime.date.today()


#   createBlock Function
#   
#   Variables:
#   name - Name of the block (String)
#   Year - Full year of the block (e.g. 2013)(Integer)
#   Month - Month number of the block (e.g. 12 for December)(Integer)
#   Day - Day of the month for the block (Integer)
#   sHour - Hour that the block starts (0-23)(Integer)
#   sMin - Minute that the block starts (0-59)(Integer)
#   eHour - Hour that the block ends (0-23)(Integer)
#   eMin - Minute that the block ends (0-59)(Integer)
#
#   Output:
#   None
#
#   Description:

#   *NOTE*
#   PLEASE RUN THE deleteSchedule FUNCTION BEFORE THIS TO AVOID DUPLICATE ENTRIES
#   This function is used to create and store a custom block into the datastore
def createBlock(name, Year, Month, Day, sHour, sMin, eHour, eMin):
    date = datetime.date(Year, Month, Day)
    sTime = datetime.time(sHour, sMin, 0)
    eTime = datetime.time(eHour, eMin, 0)
    cblock = Backend.CustomEntry.CustomEntry(name = name,
                                     sTime = sTime,
                                     eTime = eTime,
                                     date = date)
    cblock.put()


#   getSchedule Function
#
#   Variables:
#   Year - Full year of the block (e.g. 12 for December)(Integer)
#   Month - Month number of the block (Integer)
#   Day - Day of the month for the block (Integer)
#
#   Output:
#   Blocks for the inputed day, in order (List of objects)
#
#   Description:
#   This function is used to query the datastore for the schedule of any
#   date. If there is a special schedule for that date, that will be returned,
#   else, the default schedule for that day will be returned.
def getSchedule(Year, Month, Day):
    date = datetime.date(Year, Month, Day)
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


#   getToday Function
#
#   Variables:
#   None
#
#   Output:
#   Todays blocks in order (List of objects)
#
#   Description:
#   This function is used to query the datastore for todays schedule. If there is
#   a special schedule for that day, that will be returned, else the default schedule
#   will be returned.
def getToday():
    return getSchedule(today.year, today.month, today.day)


#   initBlocks Function
#
#   Variables:
#   None
#
#   Output:
#   None
#
#   Description:
#   This function is to be called in the warmup handler of the program, to instantiate
#   the entries for the default blocks into the datastore.
def initBlocks():
    Backend.addDefault.start()


#   deleteSchedule Function
#
#   Variables:
#   Year - Full year of the schedule (e.g. 12 for December)(Integer)
#   Month - Month number of the schedule (Integer)
#   Day - Day of the month for the schedule (Integer)
#
#   Output:
#   None
#
#   Description:
#   This function is used to delete all special blocks that already exist for a certain day.
#   The purpose of this is to prevent duplicate entries for a day. Please run this before
#   running the createBlock function.
def deleteSchedule(Year, Month, Day):
    date = datetime.date(Year, Month, Day)
    q = Backend.CustomEntry.CustomEntry.all()
    q.filter("date =", date).order("sTime")
    db.delete(q)