import model

# given two times, determine whether or not the current time fits in that window
def now(sTime, eTime):
    current = model.getTime().time()
    if current >= sTime and current <= eTime:
        return True
    else:
        return False

# given a schedule list, determine the current block and return its model
def current_block(schedule_list):
    for i in schedule_list:
        if i.isnow() == True:
            return i

def next_block(schedule_list):
    current = model.getTime().time()
    for i in schedule_list:
        if current <= i.sTime:
            return i

def testsblock(block):
    # try:
    #     block.isnow()
    # except RuntimeError:
    #     return ""
    # return block.formsTime()
    if block == None:
        return ""
    return block.formsTime()

def testeblock(block):
    # try:
    #     block.isnow()
    # except RuntimeError:
    #     return ""
    # return block.formeTime()
    if block == None:
        return ""
    return block.formeTime()