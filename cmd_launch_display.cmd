timeout 1
start Powershell -WindowStyle Hidden -Command py scripts\rapper.py -m 'script_display.myscript' -n 'display' -g 'group1\' -l True -r False
::cmd /k