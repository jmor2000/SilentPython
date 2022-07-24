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

# Usage
Concept
![alt text](https://github.com/jmor2000/SilentPython/blob/eff18374352fda133cb19c917335cd9111257aee/img/SP%20Scope.JPG?raw=true)

Architecture
![alt text](https://github.com/jmor2000/SilentPython/blob/db88932ce6032c21e34c71e9dce0a891bf5bc359/img/Architecture.PNG?raw=true)

Launcher
![alt text](https://github.com/jmor2000/SilentPython/blob/9f0ab07e4220a9483fabd02aca8e6d51bb3b33be/img/Launch%20Script.JPG?raw=true)

Graphical User Interface (GUI)
![alt text](https://github.com/jmor2000/SilentPython/blob/744e206cb2ec94538453e8ecc8398d7f95f2568f/img/HTML-Display.PNG?raw=true)
>- Name          - Unique name given to the script executing
>- Module        - Address in the root folder of the module/script to deploy
>- PID           - Process ID of the instance of the script running
>- Group1        - Tier1 Group Name
>- Group2        - Tier2 Group Name
>- Group3        - Tier3 Group Name
>- Status        - Status of the script instance, defined by the rapper (-1 'dead', 0 'off', 1 'ok')
>- Status        - State of the script executing, defined by the specific script ('starting', 'ok', 'error')
>- Timeout       - Intigator for whether the script has timed out (e.g Current time - TS_updated is greater than 60sec)
>- Timecount     - Time difference in seconds betwween Current time and TS_updated
>- Cyclecount    - The cycle count of a script, defined unique in each script (e.g how many data points have been processed)
>- TS_created    - Timestamp of when the script was launched
>- TS_updated    - Timestamp of the last update saved to the SQLightDB, acts as a heartbeat to monitor for timeouts
>- Log Dir       - Link to the log directory/file the script is writing its terminal to if --logfile or -l is True
>- Auto Restart  - Defines whether auto restart is enabled, --autorestart or -r is True
>- Restart Count - Counts how many restarts have been attempted (currently max is set to 3)

### Installation (bootstrapping)

Tested with:
- Windows 10 x64 OS
- python-3.10
- CMD Terminal
- PowerShell Terminal
- Google Chrome
- MQTT Mosquitto 2.0.14 (not included)
- InfluxDB 2.1.1 (not included)
- Grafana (not included)

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

### Current Modules

SilentPython\scripts\**script_Helloworld**
> Simple example script prints "Helloworld" to the terminal, good for testing.

SilentPython\scripts\**script_MQTT**
> Simple MQTT client, utilises multi threading for data acquisition (MQTT), processing (can be anything), and storage (InfluxDB).

SilentPython\scripts\**script_OPCUA**(not included)
> Simple OPC UA client, utilises multi threading for data acquisition (OPCUA), processing (can be anything), and storage (InfluxDB).

-----------------------------------------------------------------------------------


