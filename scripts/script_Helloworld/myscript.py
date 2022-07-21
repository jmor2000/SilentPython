#.......................... Standard imports
import time
import sys
from datetime import datetime

#.......................... Service
def main(sqlclient, appname="", property={}):
    #Setup
    cyclecount = 0

    #...................SQL Manager Update
    dtime = datetime.timestamp(datetime.now()) #...........State output
    items = {'state' : "starting", 'ts_updated' : dtime}
    sqlclient.sql_update(items)

    time.sleep(5)  
   bvcbvcbvcbvcbvc
   #Loop
    while True:                 
        time.sleep(1)       

        #....................Functional code
        dstate = "ok"
        cyclecount += 1
        print(f'{appname} - Hello World')

        #...................SQL Manager Update
        dtime = datetime.timestamp(datetime.now()) #...........State output
        items = {'state' : dstate, 'ts_updated' : dtime, 'count_cycle' : cyclecount}
        sqlclient.sql_update(items)
        #...................Log flush to file
        sys.stdout.flush() #outputs the termanl to the logs
