# grepIP
![Screenshot 2024-06-26 at 4.11.21 AM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/1d077ee3-1eb6-439c-8a12-9eedb585b582")
#### (formerly called "showmyip")  
Swift Python tool for instantly displaying your machine’s IP address.  
Ideal for quick network checks and troubleshooting.  
#### Alternative methods to display IP address:  
1. ```Third-party sites/software```  
Requires server connection to ping the machine and the company stores the data  
2. ```Command-Line Interface```  
Runs the _$ifconfig ..._ command, which can be complicated to decipher.  
3. ```System Settings Navigation ```  
Time-consuming to pull up system settings, time and time again.
  
However, this Python tool instantly displays your machine’s IP address, with one click quietly running the command (↓ below ↓) locally, in the background.
```diff
$ ifconfig | grep 'inet '| grep -v 127.0.0.1 | awk 'NR==1{print $2}'
```
##### Command Breakdown:
> ``` $ifconfig ```  
displays information about network interfaces on your system    
> ``` $grep 'inet ' ```  
filters for lines containing 'inet '    
> ``` $grep -v 127.0.0.1 ```   
excludes line containing '127.0.0.1' (loopback address for machine's internal use)    
> ``` $awk 'NR==1{print $2}' ```  
prints the second field from the first line of its input

## Key Functions of grepIP:
1. ``` grab_IP ```  
runs the command in the background and displays the machine's public IP address  
2. ``` reset_label ```  
once displayed, can be hidden again, and app resets

## Building Blocks:
  ``` import tkinter ```  
Module is responsible for creating the user-friendly graphical interface, giving visual appeal and interactability to the tool.  
  ``` import subprocess ```  
Module empowers tool to execute external commands (like $ifconfig and $awk) from the underlying OS shell, enabling it to interact with your network configuration.  
  ``` import pyinstaller ```  
Package used to bundle scripts into a self-contained .pkg file.  
```diff
$ cd /path/to/python/script/file/.py
$ pyinstaller --onefile --noconsole --icon='image.png' grepip.py
```
>> ``` --onefile ``` - creates a single executable file   
>> ``` --noconsole ``` - hides the console window when file executes   
>> ```--icon='image.png'``` - scrapes the folder for a file matching the name '.image.png' to assign as the file icon  
>> ```grepip.py``` - python script file  

## INSTALLATION
### A. Terminal
1. Navigate into working directory
``` diff
cd /path/to/working/dir
```  
2. Clone repo
``` diff
gh repo clone hoonc95/Data_Analytics_Portfolio
```
3. Run the app
``` diff
open showmyip
```

### B. Download ZIP
1. Click on the ![Static Badge](https://img.shields.io/badge/Code-438440) button at the top of the repo
2. Click ```Download ZIP```
3. Extract ```greipIP-main.zip```
4. Run ```showmyip```

## Full Python Script
![showmyip](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/57cfae58-3d4f-40db-8c21-58476592ca02)
