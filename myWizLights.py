import socket
import time
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
bulbs = []

def discover(broadcast,timeout=10):
	global bulbs
	bulbs = []
	message = r'{"method":"registration","params":{"phoneMac":"AAAAAAAAAAAA","register":false,"phoneIp":"1.2.3.4","id":"1"}}'
	print(message)

	sock.sendto(message.encode(), (broadcast, 38899))
	sock.setblocking(0)
	message = r'{"method":"registration","params":{"phoneMac":"AAAAAAAAAAAA","register":false,"phoneIp":"1.2.3.4","id":"1"}}'
	expire = time.time() + timeout
	while time.time() < expire:
		ready = select.select([sock], [], [], timeout)
		if ready:
			try:
				data, addr = sock.recvfrom(4096)
				print(data)
				print(addr)
				bulbs.append(addr[0])
			except:
				pass
	print("All done. Found %s bulbs at these addresses: " % (len(bulbs)))
	for bulb in bulbs:
		print(bulb)

def clampValue(value, min, max, name):
	if value < min:
		print("The min acceptable value for %s is %s" % (name,min))
		value = min
	if value > max:
		print("The max acceptable value for %s is %s" % (name,max))
		value = max
	
	return(value)

def setColor(ip, r=0, g=0, b=0, brightness=100):
	message = """{"method": "setPilot", "params": {"dimming": %s, "state": true, "r": %s, "g": %s, "b": %s}}""" % (brightness,r,g,b)
	print(message)
	r = clampValue(r, 0, 255, "r")
	g = clampValue(g, 0, 255, "g")
	b = clampValue(b, 0, 255, "b")
	brightness = clampValue(brightness, 1, 100, "brightness")
	sock.sendto(message.encode(), (ip, 38899))

def warmWhite(ip, brightness=100):
	brightness = clampValue(brightness, 1, 100, "brightness")
	message = """{"method": "setPilot", "params": {"dimming": %s, "state": true, "w": 255}}""" % (brightness)
	sock.sendto(message.encode(), (ip, 38899))

def setBrightness(ip, brightness=100):
	message = """{"method": "setPilot", "params": {"dimming": %s, "state": true}}""" % (brightness)
	print(message)
	brightness = clampValue(brightness,1,100,"brightness")
        sock.sendto(message.encode(), (ip, 38899))

def turnOn(ip):
	message = """{"method": "setPilot", "params": {"state": true}}"""
        print(message)
        sock.sendto(message.encode(), (ip, 38899))

def turnOff(ip):
        message = """{"method": "setPilot", "params": {"state": false}}""" 
        print(message)
        sock.sendto(message.encode(), (ip, 38899))
 


if __name__ == "__main__":
	print("To use this library, first call .discover(<your_broadcast_address>,<some_timeout>)")
	print("A common broadcast address would be 192.168.0.255")
	print("If your ip address is '192.168.0.100', then your broadcast is '192.168.0.255'")
	print("If your ip address is '10.4.0.200', then your broadcast is probably '10.4.0.255'")
	print("It is usually the first 3 octets of the address with 255 in the final one, as above.") 
	print("Next, look at the 'set color' function to see how to do RGB values'")
