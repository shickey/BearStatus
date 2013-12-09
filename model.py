def createcblock(name,Year,Month,Day,sHour,sMin,eHour,eMin):
  date = datetime.date(Year,Month,Day)
  sTime= datetime.time(sHour,sMin,0)
  eTime = datetime.time(eHour,eMin,0)
  cblock = customEntry(name=name,sTime=sTime, eTime=eTime,date=date)
  cblock.put()
  
  
def getSchedule(Year,Month,Day):
  date = datetime.date(Year,Month,Day)
  q = models.customEntry.all()
  q.filter("date =", today).order("sTime")
  cblocklist=[]
  blocklist=[]
  for block in q.run():
    cblocklist.append(block)
  if len(cblocklist) > 0:
    return cblocklist
  else:
    q = models.Entry.all()
    q.filter("day =", today).order("sTime")
    for block in q.run():
      blocklist.append(block)
      return blocklist
  
  
    