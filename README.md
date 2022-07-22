# Info



# Usage




### Installation (bootstrapping)
- Windows 10 x64 OS
- Python - python-3.10.5-amd64
- 
Step 1: copy and move root "SilentPython" to desired memory area
Step 2: open folder "SilentPyton\install win64"
Step 3: install python "python-3.10.5-amd64.exe"
Step 4: install dependancies with script "Installer_Script.cmd"

### Operation












-----------------------------------------------------------------------------------









# Examples
The example 1 (as seen in the image below) defines a means to:
1. Connect to a devices (TCP/IP)
2. Setup FINS communication (Handshake, exchange Nodes addresses)
3. Perform a FINS command (CMD) memory area read.

![alt text](https://github.com/jmor2000/LV-OMRON-FINS/blob/main/IMGs/Example%201.JPG?raw=true)

The device (e.g. PLC) will need to be be configure to accept FINS communition.
Please take note of the FINS node address (SD1)
In the example, the FINS header is automatically updated with client/server nodes.
This example can be modified to incorporate a wide range of other FINS commands, for reference please refere to "FINS Commands REFERENCE MANUAL" page 14 (2-1 Command List).

![alt text](https://github.com/jmor2000/LV-OMRON-FINS/blob/main/IMGs/PLC%20FINS%201.JPG?raw=true)

![alt text](https://github.com/jmor2000/LV-OMRON-FINS/blob/main/IMGs/PLC%20FINS%202.JPG?raw=true)

# Further information on Example 1, can be found:
- https://github.com/jmor2000/LV-OMRON-FINS/blob/74a2cdd1a7ba7382e7a8ce19f39bc4cab7da1dae/IMGs/Example%201%20more.JPG
- https://github.com/jmor2000/LV-OMRON-FINS/blob/74a2cdd1a7ba7382e7a8ce19f39bc4cab7da1dae/Documents/Example%201.pdf

# Referencecs:
- text
- text
