#import os
#import subprocess
#p = subprocess.Popen(["start", "cmd", "/k", "echo hello"], shell = True)
import os
import sqlite3
import time
import sys


input1_graveyard = sys.argv[1]
if input1_graveyard == 'True':
    Graveyard = True
else:
    Graveyard = False  
print(Graveyard)


#.....DB Connection
c = sqlite3.connect('file:scriptmonitor.db', uri=True)
cur = c.cursor()
#.....DB Query
cur.execute("SELECT PID,Status from scripts") #================== ASJHDAKSJHDAKSJHAKSJDHK Remove limits
script_PIDs = cur.fetchall()
print(script_PIDs)

#.....kill
killit = False

if script_PIDs != 0:
    for row in script_PIDs:
        if Graveyard == True and row[1] <1:
            killit = True
        elif Graveyard == False:
            killit = True
        
        if killit == True:
            print(row[0])
            os.system(f"""tasklist /fi "pid eq {row[0]}""")
            os.system(f"""taskkill /PID {row[0]} /F""")
            cur.execute(f"DELETE FROM scripts WHERE PID = {str(row[0])}")
            cur.connection.commit()

        #time.sleep(0.1)

