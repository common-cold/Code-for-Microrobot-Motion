import pyvisa


def connect():
    rm = pyvisa.ResourceManager()
    resource = rm.list_resources()
    inst = rm.open_resource(resource[0])
    if(len(rm.list_opened_resources())==0):
        print("Not Connected")
        rm.close()
        return
    else:
        print("Connected")
        return rm, inst


def disconnect(rm, inst):
    inst.close()
    rm.close()
    print("Disconnected")
