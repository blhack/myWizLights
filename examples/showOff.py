import myWizLights
import time

#find your broadcast IP and put it here
my_broadcast_ip = "192.168.0.255" 

#find the bulbs on your network
myWizLights.discover(my_broadcast_ip)

#turn all the bulbs to red
for bulb in myWizLights.bulbs:
	myWizLights.setColor(ip=bulb, r=255, g=0, b=0, brightness=100)
time.sleep(2)


#turn all the bulbs off
for bulb in myWizLights.bulbs:
	myWizLights.turnOff(bulb)
time.sleep(2)


#turn them all back on again
for bulb in myWizLights.bulbs:
	myWizLights.turnOn(bulb)
