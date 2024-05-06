import matplotlib.pyplot as plt
import time


def initiateArray(cycles):
    global circular
    circular =[]
    for i in range(1, cycles+1):
        circular.append((i % 2) * 0.77)

    global rect
    rect = []
    for i in range(0, cycles):
        rect.append((i % 2) * 1.39)


# def runProgram(exit_event,inst,period,cycles):
#     t1 = time.perf_counter()
#     initiateArray(cycles)
#     resetValues(inst)
#     for i in range(cycles):
#         if exit_event.is_set():
#             break
#         inst.write("CH1:CURR " + str(circular[i]))
#         print(str(circular[i]))
#         time.sleep(0.1)
#         inst.write('CH2:VOLT 32')
#         print("set Volt")
#         time.sleep(0.1)
#         inst.write("CH2:CURR " + str(rect[i]))
#         print(str(rect[i]))
#         time.sleep(period)
#
#     print("OK STOPPED")
#     t2 = time.perf_counter()
#     print(t2-t1)


def runProgram(exit_event,inst,period,cycles):
    t1 = time.perf_counter()
    initiateArray(cycles)
    resetValues(inst)
    for i in range(cycles):
        if exit_event.is_set():
            break
        setvalue(inst,1,0,period)
        print("new value")
        setvalue(inst,0,1,period)

    print("OK STOPPED")
    t2 = time.perf_counter()
    print(t2 - t1)



def resetValues(inst):
    inst.write('CH1:CURR 0')
    time.sleep(0.1)
    inst.write('CH1:VOLT 32')
    time.sleep(0.1)
    inst.write('CH2:CURR 0')
    time.sleep(0.1)
    inst.write('CH2:VOLT 32')
    time.sleep(0.1)

# def plot():
#     x = []
#     x.append(0)
#     xdist = 0
#     for i in circular:
#         xdist = xdist + (i / 0.77) * 1
#         x.append(xdist)
#
#     y = []
#     y.append(0)
#     ydist = 0
#     for i in rect:
#         ydist = ydist + (i / 1.39) * 1
#         y.append(ydist)
#
#     plt.plot(x, y)
#     plt.show()

def setvalue(inst, x, y, period):
    # X-axis = Circular Coil
    # Y-axis = Rectangular Coil
    if y==0:
        Ix = x * 0.77
        Iy = 0
    else:
        Ix = abs(x/y) * 0.77
        Iy = 1.39
    inst.write("CH1:CURR " + str(Ix))
    print(str(Ix))
    time.sleep(0.1)
    inst.write('CH2:VOLT 32')
    print("set Volt")
    time.sleep(0.1)
    inst.write("CH2:CURR " + str(Iy))
    print(str(Iy))
    time.sleep(period)

