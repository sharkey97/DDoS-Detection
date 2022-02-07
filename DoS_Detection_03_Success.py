import subprocess
import socket

hostname = socket.gethostname()
hostname = socket.gethostbyname(hostname)
output = subprocess.Popen(["fping",hostname,"-c 1"],stdout = subprocess.PIPE).communicate()[0]

print (output)
print("Ping successful, server is up and running")

if ('unreachable' in output):
    print("Ping is unsuccessful, would you like to scan how many incoming packets there are?")

count = -1
confirm1 = raw_input("Press y to view number of packets \nPress n to exit the program")
if confirm1 == "y":
	p = subprocess.Popen(('sudo', 'timeout', '1','tcpdump', '-l'), stdout=subprocess.PIPE)
	for row in iter(p.stdout.readline, b''):
    		#print row.rstrip()   # process here
		count += 1
		#print(count)
	print(count)
	if count > 100:
		print("This is a high number of requests in the timeframe, this is likely a DoS attack")
	else:
		print("There have been a regular number of packets recieved, this is likely not a DoS attack")
	
elif confirm1 == "n":
	exit()

    