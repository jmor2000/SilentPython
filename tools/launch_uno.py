import os 

os.system("""start cmd /k PowerShell.exe -WindowStyle Normal -Command py scripts/rapper.py -m "script_display.myscript" -n ""app_display" -g "group1\group2\group3" -l False -r False """)
os.system("""start cmd /k PowerShell.exe -WindowStyle Normal -Command py scripts/rapper.py -m "script_Helloworld.myscript" -n ""app_HelloWorld" -g "group1\group2\group3" -l False -r False """)