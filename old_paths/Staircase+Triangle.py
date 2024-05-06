import time
from colorama import Fore, Style


def initiateArray(cycles):
    global circular
    circular =[]
    for i in range(1, cycles+1):
        circular.append((i % 2) * 0.77)

    global rect
    rect = []
    for i in range(0, cycles):
        rect.append((i % 2) * 1.39)



def runProgram(exit_event,inst,period,cycles1,cycles2):
    resetValues(inst)
    for i in range(cycles1):
        print("STAIRCASE")
        for i in range(cycles2):
            if exit_event.is_set():
                break
            setvalue(inst,1,0,period)
            setvalue(inst,0,1,period)
        print("TRIANGLE")
        for i in range(cycles2):
            if exit_event.is_set():
                break
            setvalue(inst,1,1,period)
            setvalue(inst,1,-1,period)
        resetValues(inst)

    print("OK STOPPED")



def resetValues(inst):
    inst.write('CH1:CURR 0')
    time.sleep(0.1)
    inst.write('CH1:VOLT 32')
    time.sleep(0.1)
    inst.write('CH2:CURR 0')
    time.sleep(0.1)
    inst.write('CH2:VOLT 32')
    time.sleep(0.1)

def setvalue(inst, x, y, period):
    # X-axis = Circular Coil
    # Y-axis = Rectangular Coil
    if y==0:
        Ix = abs(x) * 0.22
        Iy = 0
    else:
        Ix = abs(x/y) * 0.22
        Iy = 1

    if x<0:
        print(Fore.RED + "X Negative ON" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "X Positive ON" + Style.RESET_ALL)

    if y<0:
        print(Fore.RED + "Y Negative ON" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Y Positive ON" + Style.RESET_ALL)

    print("\n"*2)

    inst.write("CH1:CURR " + str(Ix))
    # print(str(Ix))
    time.sleep(0.1)
    inst.write('CH2:VOLT 32')
    # print("set Volt")
    time.sleep(0.1)
    inst.write("CH2:CURR " + str(Iy))
    # print(str(Iy))
    time.sleep(period)