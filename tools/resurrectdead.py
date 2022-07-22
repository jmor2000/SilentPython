#import os
#import subprocess
#p = subprocess.Popen(["start", "cmd", "/k", "echo hello"], shell = True)
import os
import sqlite3
import time


#.....DB Connection
c = sqlite3.connect('file:scriptmonitor.db', uri=True)
cur = c.cursor()
#.....DB Query
cur.execute("SELECT * from scripts")
script_items = cur.fetchall()

#.....kill
killit = False

if script_items != 0:
    for obj_1 in script_items:
        #If dead
        if obj_1[6] < 1:      
            #Attempt Restart
            print(f"<=============== Attempt Resurrect:{str(obj_1[0])}")
            if str(obj_1[11]) != "None": reboot_logset = "True"; reboot_window = "Hidden"
            else: reboot_logset = "False"; reboot_window = "Normal"
            os.system(f""" Start PowerShell -WindowStyle {reboot_window} -Command py "scripts/rapper.py" -m "{str(obj_1[1])}" -n "{str(obj_1[0])}" -g "{str(obj_1[3])}\{str(obj_1[4])}\{str(obj_1[5])}" -l {reboot_logset} -r {obj_1[12]}  """)
            time.sleep(0.5)

        #time.sleep(0.1)
    print('Finished')
else:
    print('No items found')

time.sleep(5)


