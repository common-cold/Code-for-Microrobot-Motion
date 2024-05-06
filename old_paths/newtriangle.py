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



def runProgram(exit_event,inst,period,cycles):
    # initiateArray(cycles)
    resetValues(inst)
    for i in range(cycles):
        if exit_event.is_set():
            break
        setvalue(inst,1,1,period)
        # print("new value")
        setvalue(inst,1,-1,period)
        setvalue(inst, -1, 0, period)
        # print("new value")

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
    # X-axis = Rectangular Coil
    # Y-axis = Circular Coil
    if x==0:
        Ix = 0
        Iy = abs(x) * 0.22

    else:
        Ix = 1
        Iy = abs(y/x) * 0.22

    if x < 0:
        print(Fore.RED + "X Negative ON" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "X Positive ON" + Style.RESET_ALL)

    if y < 0:
        print(Fore.RED + "Y Negative ON" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Y Positive ON" + Style.RESET_ALL)

    print("\n"*2)

    inst.write("CH1:CURR " + str(Ix))
    time.sleep(0.1)
    inst.write('CH2:VOLT 32')
    time.sleep(0.1)
    inst.write("CH2:CURR " + str(Iy))
    time.sleep(period)