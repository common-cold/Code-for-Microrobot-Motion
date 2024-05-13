# Code for Microrobot Motion
Python code built to control the microrobot motion utilising PyVISA and Tkinter Libraries.

## Description
This project was built during my thesis work titled "Programming of the Magnetic Field for Autonomous Path Control of the Microrobots". 
The core functionality of this project lies in the utilisation of PyVISA to communicate with the Programmable Power Supply which powers the bi-axial Helmholtz coil setup 
and controls the magnetic microrobots to realise certain shapes and paths. A GUI built on tkinter have also been added to make the program easier to operate and abstract out all the underlying processes such as
linking the laptop to the power suppply, etc.

### Architecture of the program
<img src="https://github.com/common-cold/Code-for-Microrobot-Motion/assets/71568044/6454e358-d966-46d7-8ff5-721e56c887ff" width="300" height="300">

### Graphical USer Interface 
<img src="https://github.com/common-cold/Code-for-Microrobot-Motion/assets/71568044/8c5c1e07-7420-4dd7-aaf5-5934b6752383" width="500" height="300">


## Installing
1. Download the code from this repository.
2. Change the current directory in the program to the one in your machine in ```mainfile.py``` where you have downloaded the code.

> [!NOTE]
> IDE such as PyCharm, VS Code are preferable to run this code.

## Running
1. Connect your laptop to the Programmable Power Supply (PSD7303A).
2. After changing the directory, run the ```mainfile.py```.
3. Click on ```Search Device``` button.
4. Select the paths from the list and click ```Submit```.
5. Select the Time Period and Cycles of the path and click ```Submit```. 
6. Click on ```Run``` and keep an eye on the terminal of the IDE (to track the switch positions i.e, Negative or Positive).
7. Click on ```Stop``` to stop the program.
8. Make sure to disconnect by clicking on ```Disconnect``` after use.
