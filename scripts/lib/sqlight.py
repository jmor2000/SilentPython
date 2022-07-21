
#.......................... Standard imports ..........................
#.....................................................................
#.....................................................................
from itertools import count
import sys
import os
import sqlite3
from datetime import datetime
#.......................... Outside imports  .........................
sys.path.append('D:\Python\Monitoring Scripts\SilentPython 2\scripts')  
from lib.core import parent
#.....................................................................
#.....................................................................
#.....................................................................

class client(parent):
    def __init__(self):
        #-------inherit the methods and properties from its parent.
        super().__init__("These are the real details")
        #-------Set child properties
        self.items = {}
        self.connection = object

    #=================================================================[Connect to the database]
    def sql_connect(self):
        try:
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------     
            #----------Connect to database
            conn = sqlite3.connect('scriptmonitor.db')
            #----Report
            print ("Opened database successfully")
            #-----------------------------------search for SCRIPT Table
            try:
                #search for table
                cursor = conn.execute("SELECT name FROM scripts;")
                #----Report
                print ("Found table successfully")
            except:
                #table not found create Table
                conn.execute('''CREATE TABLE scripts
                        (
                        name TEXT NOT NULL,
                        module TEXT,
                        pid INT,
                        group1 TEXT,
                        group2 TEXT,                
                        group3 TEXT,
                        status INT,
                        state TEXT,
                        count_cycle INT,
                        ts_created TIMESTAMP,
                        ts_updated TIMESTAMP,
                        logdir TEXT,
                        autorestart INT
                        ) ''')
                print("Table created successfully")
            
            self.connection = conn
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------
            self.error.clear()       
        except Exception as e: 
            self.error.set(True, "sql_connect: " + str(e), 0)

    #=================================================================[Start table in database]
    def sql_start(self, db_script={}):
        try:
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------           
            self.items = db_script

            __item_name = self.items.get("name")
            __item_module = self.items.get("module")
            __item_pid = self.items.get("pid")
            __item_group1 = self.items.get("group")[0]
            __item_group2 = self.items.get("group")[1]
            __item_group3 = self.items.get("group")[2]
            __item_status = self.items.get("status")
            __item_state = self.items.get("state")

            __dt = datetime.now()
            __item_count_cycle = self.items.get("count_cycle")
            __item_ts_created = self.items.get("ts_created")
            __item_ts_updated = datetime.timestamp(__dt)
            __item_logdir = self.items.get("logdir")
            __item_autorestart = self.items.get("autorestart")

            #-----------------------------------check if item exists table  
            __cursor = self.connection.execute("SELECT name, pid FROM scripts WHERE name='"+__item_name+"'")
            __rows = __cursor.fetchall()
            __items = len(__rows)
            #print(str(__rows))
            
            if __items > 0:
                if __items > 1:
                    print("Error: Multi Scripts with the same name, please check display HMTL")
                    sys.exit(2)
                else:
                    #Delete ITEM
                    #print('Previous item found, deleteing item')
                    print("Previous item found in mysql attempt kill & delete")
                    os.system(f"""taskkill /PID {__rows[0][1]} /F""")
                    self.connection.execute("DELETE FROM scripts WHERE name='"+__item_name+"'")

            #-----------------------------------add row
            self.connection.execute(
                "INSERT INTO scripts (name,module,pid,group1,group2,group3,status,state,count_cycle,ts_created,ts_updated,logdir,autorestart) \
                VALUES ('"
                +__item_name+"','"
                +__item_module+"','"
                +str(__item_pid)+ "','"
                +__item_group1+ "','"
                +__item_group2+ "','"
                +__item_group3+ "','"
                +str(__item_status)+ "','"
                +str(__item_state)+ "','"
                +str(__item_count_cycle)+ "','"
                +str(__item_ts_created)+ "','"
                +str(__item_ts_updated)+ "','"
                +str(__item_logdir)+ "','"       
                +str(__item_autorestart)    
                +"') ")

            self.connection.commit() #<<<<<<<COMMIT

            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------
            self.error.clear()
        except Exception as e: 
            self.error.set(True, "sql_start: " + str(e), 0)

    #=================================================================[Update table in database]
    def sql_update(self,new_items={}):
        try:
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------
            #.....Update Items
            if len(new_items) > 0:              
                self.items.update(new_items)
                __item_name = self.items.get("name")
                __dt = datetime.now()
                __item_ts_updated = datetime.timestamp(__dt)
                new_items.update({"ts_updated" : str(__item_ts_updated)})

                #-----------------------------------add row
                #crreate where statement
                __statement = ""
                for ix in new_items:
                    __statement += f" {ix} = '{self.items[ix]}',"
                __statement = __statement[:-1]
                __fullstatment = f"UPDATE scripts SET {__statement} WHERE name='{__item_name}';"
                #print(__fullstatment)

                self.connection.execute(__fullstatment)
                self.connection.commit() #<<<<<<<COMMIT

                #--------------------------------------------------------------------------------
                #--------------------------------------------------------------------------------
                #--------------------------------------------------------------------------------
                self.error.clear()

        except Exception as e: 
            print(f"Error : sql update, '{e}'")
            self.error.set(True, "sql_update: " + str(e), 0)

#.... Test
if __name__ == "__main__":
    print('Python Script==========================================')
    mycore = client()
    print(mycore.details)
    mycore.sql_start({})
    print(mycore.error.get())
    print(mycore.error.signal())
    print(mycore.error.signal())
    mycore.error.set(False,'',0) #RESET
    mycore.error.set(True,'error ddddd',6666) #Set
    print(mycore.error.get())
    print(mycore.error.signal())
    print(mycore.error.signal())

    # mycore.sql_start()
    # print(mycore.error.get())
    # print(mycore.error.signal())
    # print(mycore.error.signal())
