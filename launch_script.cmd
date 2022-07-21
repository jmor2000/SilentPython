@echo off 
echo %1 
echo %2 
echo %3
echo %4
echo %5
echo %6
PowerShell.exe -WindowStyle Hidden -Command py '%1' -m '%2' -n '%3' -g '%4' -l %5 -r %6