My App
======
Final Project: Flask
<br />
To run the flask files run
```Powershell
pip install virtualenv
```
<br />
Then run
```Powershell
virtualenv myenv
```
Then lastly active your virtual environment
```Powershell
source virtualenv_name/bin/activate
```
Then github pull the flask files in it3038c-scripts
Lastly cd into the correct location in your virtual environment and run
```Python
python .\web.py
```
Hopefully the server works correctly and go to localhost:5000 to check out the flask web pages.


Remote.ps1:
This script is a practice script for Project 2 in scripting class. 
<br />
This script takes basic machine info from a computer and output's it into a location you set in Line 2 of the script
<br />
To run this script CD into the directory in VS and enter:
<br />
```Powershell
.\Remote.ps1
```
After this go to the location you set and you should see a file named "Information".
<br />
Once you learn PSRemoting you can use a script like this to run on a remote machine take the information and send it to the log file.
<br />
From here you could use the output log file to enter information of the computer into a database or something.
<br />
<br />
Lab 7:
This script is a simple script that allows you to BLUR, EMBOSS, or SHARPEN an image.
To use this script you want to begin by installing PILLOW for Python.
In your python terminal in VSCODE type in the following commands:
```PowerShell
python -m pip install --upgrade Pillow
python -m pip install --upgrade pip setuptools wheel
python -m ensurepip --default-pip
```
To see if pip is installed type
```PowerShell
python -m pip
```
Now that we have Pillow installed head over to my Lab7 folder and git pull the folder.
Once you have the folder in your visual studio code in your powershell terminal.
```PowerShell
cd Lab7
```
Now you are working inside the folder with the script. From here you can drag and drop images directly into the Lab7 folder.
Now you are ready to run the script.
```Python
python PillowTesting.py
```
From here the script will ask you what image you would like to select and if you would like to BLUR, EMBOSS, or SHARPEN.
