import importlib
import os
from tkinter import *
import subprocess
import threading

from PoweSupplyConfig import *

os.chdir("C:\\Users\\Kanhu\\Desktop\\PhD Work\\Helmholtz coil with code\\Code for motion")

exit_event = threading.Event()

resources = []


#
#
#
#
# def submitPeriod():
#
#
#
# def submitAmplitude():
#
#
# def submitCycle():
#
#

isCombination = False


def submitPath():
    global file
    file = value_inside.get()
    global isCombination
    isCombination = file.find("+") != -1
    print(isCombination)
    if isCombination:
        cycleLabel2.grid(row=4, column=2)
        cycleEntry2.grid(row=4, column=3)



def submit():
    global period
    #global amplitude
    global cycles
    period = periodEntry.get()
    #amplitude = amplitudeEntry.get()
    cycles = cycleEntry.get()
    if isCombination:
        global cycles2
        cycles2 = cycleEntry2.get()
        print(cycles2)
        print(cycles)


def run_program(stopButton):
    global pkg
    # p = subprocess.Popen(["python", file+".py", period, amplitude, cycles])
    moduleName = "paths."+file
    pkg = importlib.import_module(moduleName)

    runButton["state"] = DISABLED
    stopButton["state"] = NORMAL

    runPrg = getattr(pkg, "runProgram")

    if isCombination:
        t1 = threading.Thread(target=runPrg,args=[exit_event,inst,int(period),int(cycles),int(cycles2)])
    else:
        t1 = threading.Thread(target=runPrg,args=[exit_event,inst,int(period),int(cycles)])
    # if not t1.is_alive():
    #     t1 = None
    #     t1 = threading.Thread(target=runPrg, args=[exit_event, inst, int(period), int(cycles)])
    t1.start()

    runButton["state"] = NORMAL

def connectDevice():
    global rm, inst
    rm, inst = connect()

def disconnectDevice():
    disconnect(rm, inst)


def stop_program():
    exit_event.set()
    runButton["state"] = NORMAL
    t1 = None
    print("stopped")


window = Tk()
window.geometry("450x255")

options = ["Staircase", "TriangularPath", "Staircase+Triangle", "Square_Shape", "Triangle_Shape", "A_shape", "M_shape", "N_shape"]
# options = ["TriangularPath", "Staircase", "M_shape", "A_shape", "N_shape", "Square_Shape"]

connectButton = Button(window,text="Search device",font=("Aerial",9),command=connectDevice)
connectButton.grid(row=0,column=0,padx=10,pady=10)


disconnectButton = Button(window,text="Disconnect",font=("Aerial",9),command=disconnectDevice)
disconnectButton.grid(row=0,column=3,padx=0,pady=10)


value_inside = StringVar(window)
value_inside.set("Select the path")

dropDown = OptionMenu(window, value_inside, *options)
dropDown.grid(row=1,column=0,columnspan=3,padx=10,pady=10)
PathButton = Button(window, text="Submit",font=("Aerial",9), command=submitPath).grid(row=1,column=2)

periodLabel = Label(window,text="Time Period: ",font=("Aerial",11)).grid(row=2,column=0)
periodEntry = Entry(window)
periodEntry.grid(row=2,column=1,padx=10,pady=10)
#periodButton = Button(window, text="Submit", command=submitPeriod).grid(row=2,column=2)

# amplitudeLabel = Label(window,text="Amplitude: ",font=("Aerial",10)).grid(row=3,column=0)
# amplitudeEntry = Entry(window)
# amplitudeEntry.grid(row=3,column=1)
#amplitudeButton = Button(window, text="Submit", command=submitAmplitude).grid(row=3,column=2)

cycleLabel = Label(window,text="Total Cycles: ",font=("Aerial",11)).grid(row=4,column=0)
cycleEntry = Entry(window)
cycleEntry.grid(row=4,column=1,padx=10,pady=10)
#cycleButton = Button(window, text="Submit", command=submitCycle).grid(row=4,column=2)

cycleLabel2 = Label(window, text="Individual Cycles: ", font=("Aerial", 11))
cycleEntry2 = Entry(window)
cycleLabel2.grid_forget()
cycleEntry2.grid_forget()



runButton = Button(window,text="Run", font=("Aerial",9), command= lambda: run_program(stopButton))
runButton.grid(row=6,column=0,padx=0,pady=6)

submitButton =  Button(window,text="Submit", font=("Aerial", 9), command=submit).grid(row=5,column=1,padx=10,pady=0)

stopButton = Button(window,text="Stop", font=("Aerial",9), command= stop_program,state=DISABLED)
stopButton.grid(row=6,column=2,padx=0,pady=6)




window.mainloop()
