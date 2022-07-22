# Info



# Usage




### Installation (bootstrapping)

Tested with:
- Windows 10 x64 OS
- CMD Terminal
- PowerShell Terminal
- Google Chrome
- MQTT Mosquitto 2.0.14 (not included)

Steps:
,,,
- Step 1: copy and move root "SilentPython" to desired memory area
- Step 2: open folder "SilentPyton\install win64"
- Step 3: install python "python-3.10.5-amd64.exe"
- Step 4: install dependancies with script "Installer_Script.cmd"
,,,

### Operation

**Quick CMD Terminal Commands

cmd_launch_display.cmd
> Launches the HTML Display Script.
  
cmd_launch_batchMQTT.cmd
> Luanches a batch of MQTT scripts.

cmd_launch_batchHelloWorld.cmd
> Luanches a batch of HelloWorld scripts.

cmd_killall.cmd
> Loads the SQLight DB and kills all the items through PID terminate.

cmd_killgravedigger.cmd
> Loads the SQLight DB and kills all "dead" scripts and remove them from DB.
  
cmd_resurrectdead.cmd
> Loads the SQLight DB and attempts to re-launch "dead" scripts

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
