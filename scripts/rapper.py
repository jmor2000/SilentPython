import getopt
from itertools import count
import sys
import os
from datetime import datetime
import importlib
import lib.sqlight



#=============================================================================== Functions
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

#--------------------------------Extract data from CMD execute
def passdata(argv):
    arg_name = "unknown"
    arg_module = ""
    arg_group = []
    arg_logfile = False
    arg_autorestart = 0
    arg_help = "{0} -m <module name> -n <script name> -g <grouping g1\g2\g3> -l <log file?>".format(argv[0])
    return_data = {}
    
    try:
        opts, args = getopt.getopt(argv[1:], "hm:n:g:l:r:", ["help", "module=", "name=", "group=", "logfile=", "autorestart="])
    except:
        print(arg_help)
        sys.exit(2)
    
    #decode variables set
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-m", "--module"):
            arg_module = arg
        elif opt in ("-n", "--name"):
            arg_name = arg
        elif opt in ("-g", "--group"):
            arg_group = arg.split("\\",3) #Split group items
            quick_c = len(arg_group)
            if quick_c == 0: arg_group.extend(['','',''])
            elif quick_c == 1: arg_group.extend(['',''])
            elif quick_c == 2: arg_group.extend([''])
            print(arg_group)

        elif opt in ("-l", "--logfile"):
            if arg == "True": arg_logfile = True
        elif opt in ("-r", "--autorestart"):
            if arg == "True": arg_autorestart = 1
    
    #check for name
    if arg_name == "unknown":
        sys.exit("Error: Please Set a Name -n")
    elif arg_module == "":
        sys.exit("Error: Please Set a Module -m")

    #set return values
    #arg_module = arg_module + ".myscript"
    return_data.update({'module' : arg_module})
    return_data.update({'name' : arg_name})
    return_data.update({'group' : arg_group})
    return_data.update({'logfile' : arg_logfile})
    return_data.update({'autorestart' : arg_autorestart}) 

    return return_data

#=============================================================================== Main Execute
    #----------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------
if __name__ == "__main__":
    #Get input data
    print('Python Script==========================================')
    #get the inputs
    script_config = passdata(sys.argv)
    #set some key var
    appname = script_config.get("name")
    ts = datetime.now()
    ts_created = datetime.timestamp(ts)
    ts_created_b = ts.strftime("%Y_%m_%d-%H_%M_%S")

    #setup log directory
    if script_config['logfile'] == True:
        cwd = os.getcwd()
        dir = os.path.join(cwd, "logs", appname)
        dir_log = f"{dir}/{ts_created_b}.log"
        os.makedirs(dir, exist_ok = True)

        #output the logs
        print(f'Switching terminal to output into logfile: {dir_log}')
        logs_output_to_file = open(dir_log, 'w')
        sys.stdout = logs_output_to_file
        script_config.update({'logdir' : dir_log})

    print(f'Started at: {ts_created}')

    #--------------------------------------------Script Display
    script_config.update({'pid' : os.getpid()})
    script_config.update({'status' : 1})
    script_config.update({'state' : "starting"})

    script_config.update({'ts_created' : ts_created})
    script_config.update({'count_cycle' : 0})
    #Connect to DB
    sql_client = lib.sqlight.client()
    sql_client.sql_connect()
    #Update DB
    sql_client.sql_start(script_config)

    #record
    print('Display Script Successfully Updated in SQLight')
    print(script_config)

    #----------------------------------------------------------

    #========================================================================= Execute script    
    #----------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------
    try:
        #--------------------Dynamic Import
        print("try import......." + script_config.get('module'))
        myscript = importlib.import_module(script_config.get('module'))
        myscript.main(sql_client,appname,{})
    except Exception as e: 
        print(e)
    
    #==================================================================================== END  
    #----------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------
    
    #--------------------------------------------Script Display
    items = {'status' : -1, 'ts_updated' : datetime.timestamp(datetime.now())}
    sql_client.sql_update(items)

    print('Display Script Successfully Updated in SQLight')
    #----------------------------------------------------------
 
    print('Python Script==========================================')
    print('End')
    sys.stdout.flush()
    
    if script_config['logfile'] == True:
        logs_output_to_file.close()