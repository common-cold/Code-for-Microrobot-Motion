import time
from colorama import Fore, Style


def runProgram(exit_event, inst, period, cycles):
    resetValues(inst)
    for i in range(cycles):
        if exit_event.is_set():
            break
        setvalue(inst, 1, 0, period)
        setvalue(inst, 0, -1, period)
        setvalue(inst, -1, 0, period)
        setvalue(inst, 0, 1, period)

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
    if x == 0:
        Ix = 0
        Iy = abs(y) * 0.2

    else:
        Ix = 1
        Iy = abs(y / x) * 0.2

    if x < 0:
        print(Fore.RED + "X Negative ON" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "X Positive ON" + Style.RESET_ALL)

    if y < 0:
        print(Fore.RED + "Y Negative ON" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Y Positive ON" + Style.RESET_ALL)

    print("\n" * 2)

    inst.write("CH1:CURR " + str(Ix))
    time.sleep(0.1)
    inst.write('CH2:VOLT 32')
    time.sleep(0.1)
    inst.write("CH2:CURR " + str(Iy))
    time.sleep(period)