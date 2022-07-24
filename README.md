# Info

SilentPython:
- is a light weight microservice framework which supports the backend deployment and management of 100s of independent continuously operating python scripts in a windows OS environment. 
- enables the silent execution (hidden terminal) of independent python scripts/modules, and provides an independent HTML Graphical User Interface(GUI) to monitor the scripts status, and vie the terminal output of each script.
- was created to overcome challenges when deploying independent scripts on scale and over time, including, how to:
    1. quick deploy scripts dynamically and operate them in the background (silently)
    2. how to group related scripts, and monitor their status, operation, and key metrics
    3. how to make scripts more robust (reboot capability)
    4. how to create and destroy executing scripts on demand (PID)
- intended use is for industrial applications, in which activities need to be multi-purpose, robust, self-healing, ever evolving, and scaling.

![alt text](img/SP Scope.JPG?raw=true)

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
- InfluxDB 2.1.1 (not included)

Steps:
- Step 1: copy and move root "SilentPython" to desired memory area
- Step 2: open folder "SilentPyton\install win64"
- Step 3: install python "python-3.10.5-amd64.exe"
- Step 4: install dependancies with script "Installer_Script.cmd"

### Operation

**Quick CMD Terminal Commands**

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


