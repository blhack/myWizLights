# My Wiz Lights

Interacting with these lights is extremely simple.  You can read through the code in myWizLights.py to see how it is done.
Generally: convert a json object to a string, and send it to the IP address of a light over UDP on port 38899.

## How to use

```python
import myWizLights

#find your broadcast IP and put it here
my_broadcast_ip = "192.168.0.255" 

#find the bulbs on your network
myWizLights.discover()

#turn all the bulbs to red
for bulb in myWizLights.bulbs:
	myWizLights.setColor(ip=bulb, r=255, g=0, b=0, brightness=100)

#turn all the bulbs off
for bulb in myWizLights.bulbs:
	myWizLights.turnOff(bulb)

#turn them all back on again
for bulb in myWizLights.bulbs:
	myWizLights.turnOn(bulb)
```

## Also
The "bulbs" list is just a list of IP addresses.  If you know the IP addresses of your bulbs (which you can find in the app) you could start making groups and thigns here.
For instance:

```python
import myWizLights

outsideLights = ["10.69.0.10","10.69.0.11","10.69.0.12","10.69.0.13"]
insideLights = ["10.69.0.20","10.69.0.21","10.69.0.22","10.69.0.23"]

#turn off all the lights inside
for bulb in insideLights:
	myWizLights.turnOff(bulb)

#turn on all the lights outside
for bulb in outsideLights:
	myWizLights.turnOn(bulb)
