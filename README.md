# Nuclear Probe Repository for the Proton Probers, 01/2024 - 05/2024

This repository will be updated over the specified window to contain the resarch, code, and design schematics of our team over the competition window. **Future competitors are encouraged to take inspiration from our findings and improve on our designs.**

## Section 1: Project Design

## Section 2: Code

### Arduino
The technical aspects of the project are contained in the **code/** directory. The **photodiode_test/** directory contains the arduino file which must be compiled using the arduino editor. Our code was written for the **Arduino Uno**, so **please adapt the photodiode_test/photodiode_test.ino code to suit your arduino and photodiode configuration**.

### Python
Second, I will outline the use of the python file here. The recommended way to run the file is to access the file in **code/CerenkovListener.py** and run the file in a command line using the command **>>python CerenkovListener.py -p [PORT] -r [BITRATE] -f [Filename]** at low privilige (administrator/sudo not necessary). Ensure that the specified port matches the communication port in the arduino IDE. The COM port bitrate set in our *photodiode_test.ino* file is 9600 bits/second, but if yours is different, specify it here. 

If you want to run the python program quickly, it can also be run using **>> python CerenkovListener.py -f [Filename]**.  If you change the COM and Bitrate values in the arduino file, you can **edit the default parameter values within listen()** to match your changes so that this command configuration works as intended. 

### Linear regression

## Section 3: FEDD Day
