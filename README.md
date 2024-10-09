# grepIP
![Screenshot 2024-06-26 at 4.11.21 AM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/1d077ee3-1eb6-439c-8a12-9eedb585b582")
### (formerly called "showmyip")  
A swift and simple Python tool used to instantly display your machine's IP address. Ideal for quick network checks and troubleshooting.
There are at least 3 main ways to display a machine's IP address - Third-party websites/software | Command-Line Interface | "Settings > WiFi > More Info".  
- [Third-party sites/software] requires connected to a server to ping the machine, where the company will hold that data  
- [Command-Line Interface] requires a command (_$ ifconfig_) / a string of commands (_below_) - difficult to decipher/memorize
- [WiFi Settings] takes time to locate the correct option and buttons  
  
However - at the click of single button - this packaged python tool display your machine's IP address by running the following (↓ below ↓) into the terminal (in the background).
```diff
$ ifconfig | grep 'inet '| grep -v 127.0.0.1 | awk 'NR==1{print $2}'
```
## Breakdown of Command:
#### _ifconfig_  
displays information about network interfaces on your system  
#### _grep 'inet '_  
filters for lines containing 'inet '  
#### _grep -v 127.0.0.1_  
excludes line containing '127.0.0.1' (loopback address for machine's internal use)  
#### _awk 'NR==1{print $2}'_  
prints the second field from the first line of its input

## Key functions:
#### _grab_IP_  
run the command in the background and display the "Public IP" address  
#### _reset_label_
once IP is displayed, can be hidden again, and app resets

## Building blocks:
#### _tkinter_
Module is responsible for creating the user-friendly graphical interface, giving visual appeal and interactability to the tool.  
#### _subprocess_
Module empowers tool to execute external commands (like $ifconfig and $awk) from the underlying OS shell, enabling it to interact with your network configuration.  
#### _pyinstaller_
Package used to bundle scripts into a self-contained .pkg file.  
```diff
$ cd /path/to/python/script/file/.py
$ pyinstaller --onefile --noconsole --icon='image.png' grepip.py
```
_--onefile_ - creates a single executable file   
_--noconsole_ - hides the console window when file executes   
_--icon='image.png'_ - scrapes the folder for a file matching the name '.image.png' to assign as the file icon  
_grepip.py_ - python script file  
## Full Python Script
![showmyip](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/57cfae58-3d4f-40db-8c21-58476592ca02)
