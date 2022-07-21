
import time
from datetime import datetime
import sys
import psutil
import os
#--------------------------------Extract data from CMD execute
def html_update(Table=""):

    # to open/create a new html file in the write mode
    f = open('Display.html', 'w')

    # Inputs
    html_Heading = "Python Script Table"
    html_Table = Table

    # the html code which will go in the file GFG.html
    html_style_tdth = """{border: 1px solid; padding: 8px;}"""
    html_style_table = """{width: 100%; border-collapse: collapse;}"""
    html_style_tr = """nth-child(even) {background-color: #f2f2f2;}"""
    html_style_thead = """{background-color: #AEC9F5;}"""

    #<meta http-equiv='refresh' content='10'>    
    html_template = f"""
    <html>
        <head>
            <style>
                td, th {html_style_tdth}
                table {html_style_table}
                tr:{html_style_tr}
                thead {html_style_thead}
            </style>           
        </head>
        <body>
            <h2>{html_Heading}</h2>
            <input type="text" id="Input1" onkeyup="myFunction(0, 'Input1')" placeholder="Filter: Name">
            <input type="text" id="Input2" onkeyup="myFunction(3, 'Input2')" placeholder="Filter: Group1">
            <p>This table is a list of all the python scripts running that are connected to SQLight</p>
            {html_Table}
        </body>
    </html>
    """ + """
    <script>
    function myFunction(column_inx, mystring) {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(mystring);
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[column_inx];
        if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
        }
    }
    }
    </script>
    """
   
    # writing the code into the file
    f.write(html_template)
    f.close()

#--------------------------------Main Execute
def main(sqlclient, appname="", property={}):
    #.....DB Connection
    #c = sqlite3.connect('file:scriptmonitor.db?mode=ro', uri=True)
    cur = sqlclient.connection.cursor()
    G_count_cycle = 0
    dict_PIDead = []
    dict_Name = {}

    #=======WAIT
    while True:

        #.....DB Query
        cur.execute("SELECT * from scripts")
        getallitems = cur.fetchall()
        #Print(test)
        #.....Timestamp
        __mytime = datetime.now()
        CurrentTime = datetime.timestamp(__mytime)
        timeout_time = 60 #<-----------------------------------------------------timeout

        #HMTL...TABLE\\\\\\\\\\\\\\\\\\\\\\\\\\\
        table = """<div style="overflow-x: auto;">\n"""
        table += """<table id="myTable">\n"""
        #HTML............Headings
        table += "<thead>\n"
        theaders = ['Name','Module','PID', 'Group1', 'Group2','Group3','Status','State', 'Timeout', 'Timecount', 'Cyclecount', 'TS_created', 'TS_updated', 'Log Dir', 'Auto Restart', 'Restart Count']
        for thead in theaders:
            table += f"    <td>{thead}</td>\n"
        #HTML............Body
        table += "  <tbody>\n"
        for obj_1 in getallitems:
            #Conversions
            item_name = str(obj_1[0])
            item_currenttime = datetime.fromtimestamp(CurrentTime)
            item_ts_created = datetime.fromtimestamp(obj_1[9]).strftime("%d/%m/%Y %H:%M:%S")
            item_ts_updated = datetime.fromtimestamp(obj_1[10]).strftime("%d/%m/%Y %H:%M:%S")          
            item_timeout_time = int(CurrentTime - obj_1[10])
            item_logdir = obj_1[11]
            item_autorestart = obj_1[12]
            item_autorestart_str = 'True' if obj_1[12] == True else 'False'
            item_autorestart_count = 0

            #Script Check: PID
            if item_timeout_time > timeout_time:
                item_timeout_str = 'timeout'
                if obj_1[6] > 0:
                    combo_name = item_name + "_" + str(obj_1[2])
                    if not combo_name in dict_PIDead:
                        PID_Exist = psutil.pid_exists(int(obj_1[2]))
                        if PID_Exist == False: 
                            dict_PIDead.append(combo_name)
                            print(f"..........This script:{combo_name} is DEAD")
                            #...................SQL Manager Update.............
                            fullstatment = f"UPDATE scripts SET Status=0 WHERE Pid={int(obj_1[2])};"
                            sqlclient.connection.execute(fullstatment)
                            #..................................................'
                    else:
                        PID_Exist = False
                else:
                    PID_Exist = True #status == error
            else:
                item_timeout_str = 'ok'
                PID_Exist = True

            #Script Check: Status
            if obj_1[6] == 1:
                item_status = 'ok'
            elif obj_1[6] == -1:
                item_status = 'error'
            elif obj_1[6] == 0:
                item_status = 'dead'               
            else: 'unknown'


            #Script Check: Restart
            if item_name in dict_Name:
                item_autorestart_count = dict_Name[item_name]
                if item_status != 'ok' and item_timeout_str == 'timeout' and item_autorestart == True:
                    if item_autorestart_count < 3:
                        #Attempt Restart
                        print(f"<=============== Attempt Restart:{item_name}")
                        print(str(item_logdir))
                        if str(item_logdir) != "None": reboot_logset = "True"; reboot_window = "Hidden"
                        else: reboot_logset = "False"; reboot_window = "Normal"
                        os.system(f""" start cmd /k PowerShell.exe -WindowStyle {reboot_window} -Command py scripts/rapper.py -m "{str(obj_1[1])}" -n "{str(obj_1[0])}" -g "{str(obj_1[3])}\{str(obj_1[4])}\{str(obj_1[5])}" -l {reboot_logset} -r True  """)
                        item_autorestart_count += 1
                        dict_Name.update({item_name : item_autorestart_count})
            else:
                dict_Name.update({item_name : 0})

            #..........................................................................................         
            #Outputs
            table += "  <tr>\n"
            table += f"    <td>{str(obj_1[0])}</td>\n"
            table += f"    <td>{str(obj_1[1])}</td>\n"
            table += f"    <td>{str(obj_1[2])}</td>\n"  # PID          
            table += f"    <td>{str(obj_1[3])}</td>\n"
            table += f"    <td>{str(obj_1[4])}</td>\n"   
            table += f"    <td>{str(obj_1[5])}</td>\n"
            table += f"    <td style='background-color:{status_color(item_status)}'>{str(item_status)}</td>\n"
            table += f"    <td style='background-color:{status_color(obj_1[7])}'>{str(obj_1[7])}</td>\n"
            table += f"    <td style='background-color:{status_color(item_timeout_str)}'>{str(item_timeout_str)}</td>\n"
            table += f"    <td>{str(item_timeout_time)}</td>\n"     # Timeout Count
            table += f"    <td>{str(obj_1[8])}</td>\n"              # Cycle Count                      
            table += f"    <td>{str(item_ts_created)}</td>\n"
            table += f"    <td>{str(item_ts_updated)}</td>\n"
            table += f"    <td><a href='{str(item_logdir)}'>link Log</a></td>\n"
            table += f"    <td>{str(item_autorestart_str)}</td>\n"
            table += f"    <td>{str(item_autorestart_count)}</td>\n"           
        table += "  </tr>\n"

            #for item in obj_1:
            #    table += f"    <td>{str(item)}</td>\n"
        table += "  </tbody>\n"

        #HMTL...TABLE\\\\\\\\\\\\\\\\\\\\\\\\
        table += "</table>\n" 
        table += "</div>\n"
        table += f"\nCurrent Time:{item_currenttime}\n"      

        html_update(table)
        #...................................
        G_count_cycle += 1 # Count the Cycle
        #...................................
        #--------------------------------------------Script Display
        items = {'status' : 1, 'state' : 'ok', 'ts_updated' : datetime.timestamp(datetime.now()), 'count_cycle' : G_count_cycle}
        sqlclient.sql_update(items)
        print('HTML Table Updated'+str(CurrentTime))
        sys.stdout.flush()

        time.sleep(2)


#================================================= FUNCTIONS
#================================================= FUNCTIONS
#================================================= FUNCTIONS

def status_color(item):

    #This function identifies the HTML Colour, depending on
    #if it is a string or a boolean
    
    color_green = "#7FFFD4"
    color_yellow = "#FAFAD2"
    color_null = "#FFFFFF"

    colour_output = color_null

    #BOOL
    if isinstance(item, bool) == True:
        if item == True:
            colour_output = color_green
        else:
            colour_output = color_yellow

    #STRING
    if isinstance(item, str) == True:
        if item == "ok":
            colour_output = color_green
        elif item == "error" or "timeout" or "dead":
            colour_output = color_yellow
        else:
            colour_output = color_null
    
    return colour_output
