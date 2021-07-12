from django.shortcuts import render
from opcua import Server
from random import randint
import datetime
import time

# Create your views here.

UAserver = Server()
url = "opc.tcp://GOPAL-PC:8200"
UAserver.set_endpoint(url)
name = "OPC GOPAL SIM SERVER"
addspace = UAserver.register_namespace(name)
node = UAserver.get_objects_node()
Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

UAserver.start()
print("Gopal Server Started".format(url))

while True:
    Temperature = randint(33, 36)
    Pressure = randint(498, 502)
    TIME = datetime.datetime.now()

    print(TIME, Temperature, Pressure)
    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(5)
