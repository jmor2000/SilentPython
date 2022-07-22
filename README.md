# Info



# Usage
Architecture
![alt text](https://github.com/jmor2000/SilentPython/blob/db88932ce6032c21e34c71e9dce0a891bf5bc359/img/Architecture.PNG?raw=true)

Launcher
![alt text](https://github.com/jmor2000/SilentPython/blob/744e206cb2ec94538453e8ecc8398d7f95f2568f/img/Launch%20Script.JPG?raw=true)

Graphical User Interface (GUI)
![alt text](https://github.com/jmor2000/SilentPython/blob/744e206cb2ec94538453e8ecc8398d7f95f2568f/img/HTML-Display.PNG?raw=true)


### Installation (bootstrapping)

Tested with:
- Windows 10 x64 OS
- python-3.10
- CMD Terminal
- PowerShell Terminal
- Google Chrome
- MQTT Mosquitto 2.0.14 (not included)

Steps:
- Step 1: copy and move root "SilentPython" to desired memory area
- Step 2: open folder "SilentPyton\install win64"
- Step 3: install python "python-3.10.5-amd64.exe"
- Step 4: install dependancies with script "Installer_Script.cmd"

### Operation

**Quick CMD Terminal Commands**

cmd_launch_display.cmd 
> Launches the HTML Display Script.
  
cmd_launch_batchMQTT.cmd ```
> Luanches a batch of MQTT scripts.

cmd_launch_batchHelloWorld.cmd `#89d5e8
> Luanches a batch of HelloWorld scripts. ```

cmd_killall.cmd `#89d5e8`
> Loads the SQLight DB and kills all the items through PID terminate.

cmd_killgravedigger.cmd `#89d5e8`
> Loads the SQLight DB and kills all "dead" scripts and remove them from DB.
  
cmd_resurrectdead.cmd `#89d5e8`
> Loads the SQLight DB and attempts to re-launch "dead" scripts

-----------------------------------------------------------------------------------


