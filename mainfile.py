import importlib
import os
from tkinter import *
import subprocess
import threading

from PoweSupplyConfig import *

os.chdir("F:\\Python-shits\\Tkinter_Testing\\Tkinter")

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
window.geometry("500x250")

options = ["Staircase", "TriangularPath", "Staircase+Triangle", "Square_Shape", "Triangle_Shape", "A_shape", "M_shape", "N_shape"]
# options = ["TriangularPath", "Staircase", "M_shape", "A_shape", "N_shape", "Square_Shape"]

connectButton = Button(window,text="Search device",command=connectDevice)
connectButton.grid(row=0,column=0)


disconnectButton = Button(window,text="Disconnect",command=disconnectDevice)
disconnectButton.grid(row=0,column=3)


value_inside = StringVar(window)
value_inside.set("Select the path")

dropDown = OptionMenu(window, value_inside, *options)
dropDown.grid(row=1,column=0,columnspan=3)
PathButton = Button(window, text="Submit", command=submitPath).grid(row=1,column=2)

periodLabel = Label(window,text="Time Period: ",font=("Aerial",10)).grid(row=2,column=0)
periodEntry = Entry(window)
periodEntry.grid(row=2,column=1)
#periodButton = Button(window, text="Submit", command=submitPeriod).grid(row=2,column=2)

# amplitudeLabel = Label(window,text="Amplitude: ",font=("Aerial",10)).grid(row=3,column=0)
# amplitudeEntry = Entry(window)
# amplitudeEntry.grid(row=3,column=1)
#amplitudeButton = Button(window, text="Submit", command=submitAmplitude).grid(row=3,column=2)

cycleLabel = Label(window,text="Total Cycles: ",font=("Aerial",10)).grid(row=4,column=0)
cycleEntry = Entry(window)
cycleEntry.grid(row=4,column=1)
#cycleButton = Button(window, text="Submit", command=submitCycle).grid(row=4,column=2)

cycleLabel2 = Label(window, text="Individual Cycles: ", font=("Aerial", 10))
cycleEntry2 = Entry(window)
cycleLabel2.grid_forget()
cycleEntry2.grid_forget()



runButton = Button(window,text="Run",command= lambda: run_program(stopButton))
runButton.grid(row=6,column=0)

submitButton =  Button(window,text="Submit", command=submit).grid(row=5,column=1)

stopButton = Button(window,text="Stop",command= stop_program,state=DISABLED)
stopButton.grid(row=6,column=4)




window.mainloop()
